import time
import pandas as pd
import requests
from bs4 import BeautifulSoup

list_of_books = []

for number in range(1, 51):
    url = f"http://books.toscrape.com/catalogue/page-{number}.html"
    
    try:
        response = requests.get(url, timeout=10)
        if response.status_code != 200:
            print(f"Page {number}: skipped (status {response.status_code})")
            continue
            
        soup = BeautifulSoup(response.text, "html.parser")
        tables = soup.find_all("article", class_="product_pod")

        for table in tables:
            book = {
                "title": table.h3.a["title"],
                "price": table.find("p", class_="price_color").text,
                "rating": table.find("p", class_="star-rating")["class"][1],
                "availability": table.find("p", class_="instock availability").text.strip()
            }
            list_of_books.append(book)

        time.sleep(1)

    except requests.exceptions.ConnectTimeout:
        print(f"Page {number}: timed out : skipping")
        continue
    except requests.exceptions.ConnectionError:
        print(f"Page {number}: connection error : skipping")
        continue

print(f"Total books scraped: {len(list_of_books)}")
df = pd.DataFrame(list_of_books)
df.to_csv("books.csv", index=False, encoding="utf-8")

