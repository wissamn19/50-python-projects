# REST API client

> Requests, JSON parsing

## Overview
A Python script that fetches and displays Pokémon data from the PokéAPI, a free public API. Given a Pokémon name, it retrieves and prints the name, height, weight, and abilities by parsing a nested JSON response. Built to understand how HTTP requests work and how to navigate real-world API data.

## Concepts Practiced
- HTTP GET requests with the `requests` library.
- Parsing and navigating nested JSON responses.
- Working with a real public API (PokéAPI).

## How to Run
```bash
# from this folder
python main.py
```

## What I Learned

This was my first time working with a real external API and it changed how I think about data on the internet. Before this project, I didn't know what HTTP status codes were, now checking `response.status_code == 200` before touching the data feels natural. It means the request succeeded and the server is responding correctly.

The trickiest part was navigating the nested JSON response. When I first printed `response.json()` to see the raw data, it looked overwhelming, a deeply nested dictionary with lists inside dictionaries inside lists. Getting to something like `data['abilities'][0]['ability']['name']` required me to read the structure carefully layer by layer. That habit of printing the raw response first to understand the shape of the data is something I'll carry into every API project
from here.

This project also made me realize that most real world data comes through APIs exactly like this, and that `requests` plus `json` is all you need to access it.

---
[← Back to main repo](../../README.md)