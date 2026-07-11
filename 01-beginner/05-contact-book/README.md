# Contact Book with Search

> dictionaries, file persistence, fuzzy search

## Overview
A command-line contact manager that stores entries in JSON and supports full CRUD. The main goal was to move past exact-match search and use `rapidfuzz` for approximate name lookup, with a confirmation step before any update or delete so a typo can't silently touch the wrong record.

## Concepts Practiced
- dictionaries
- file persistence
- fuzzy search

## How to Run
```bash
# from this folder
python main.py
```

## What I Learned
Early in development, I encountered an issue where wrapping an input function inside a print statement **(print(input()))** erroneously assigned None to my variables. This taught me a valuable lesson about Python’s function return values and data flow.
Performance in Search Queries: Extracting elements dynamically across datasets requires careful thresholds. Using `fuzz.WRatio` allowed me to weigh strings by partial matches, which taught me how search engines prioritize relevance scores.
The Importance of Type Enforcement: I learned firsthand why interactive CLI structures require string enforcement over standard integer matching (choose == "1" vs choose == 1), as input() natively interprets all terminal keystrokes as strings.

---
[← Back to main repo](../../README.md)