import requests

base_url = "https://pokeapi.co/api/v2/"

def get_pokemon_info(name):
    url = f"{base_url}pokemon/{name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Name: {data['name']}")
        print(f"Height: {data['height']}")
        print(f"Weight: {data['weight']}")
        print("Abilities:")
        for ability in data['abilities']:
            print(f"- {ability['ability']['name']}")
    else:
        print(f"Error: Unable to fetch data for {name}. Status code: {response.status_code}")
pokemon_name = "ditto"
get_pokemon_info(pokemon_name)

