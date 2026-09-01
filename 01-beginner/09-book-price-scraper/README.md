# Web Scraper for Book Prices

> requests, BeautifulSoup, error handling, CSV

## Overview
A web scraper that extracts book titles, prices, ratings, and availability
from Books to Scrape, a site built for scraping practice. Scrapes all 50
pages, handles connection timeouts gracefully, and saves the results to a
CSV file. Collected 940 out of 1000 books, the rest were skipped due to
server timeouts, which is normal behavior for a real world scraper.

## Concepts Practiced
- HTTP requests with the `requests` library
- HTML parsing with `BeautifulSoup`
- Navigating nested HTML tags and extracting attributes
- Error handling : `ConnectTimeout`, `ConnectionError`, status codes
- Rate limiting : `time.sleep()` to avoid overwhelming the server
- Saving scraped data to CSV with Pandas

## How to Run
```bash
# from this folder
pip install -r requirements.txt
python main.py
```

## Output
A `books.csv` file with the following columns:

| Column | Example |
|--------|---------|
| title | A Light in the Attic |
| price | £51.77 |
| rating | Three |
| availability | In stock |

## What I Learned

The hardest part was navigating the HTML structure to extract the right data.
Before writing any extraction logic I had to print `soup.prettify()` to read
the raw HTML and understand where each piece of information lived, the title
was in an `<a>` tag's `title` attribute, not its text, and the rating was
hidden inside a CSS class name like `"Three"` rather than a number. Learning
to read HTML like a map was the real skill here.

The second challenge was handling real-world connection issues. My first version
had no error handling and crashed completely on page 32 when the server timed out.
Adding `try/except` with `timeout=15` and `time.sleep(3)` between requests made
the scraper resilient, it skipped timed-out pages and kept going instead of
crashing. The final result was 940 out of 1000 books, which is realistic for
a live scraper hitting a real server.

This project taught me that web scraping is less about writing code and more
about reading and understanding the structure of data you don't control.

---
[← Back to main repo](../../README.md)