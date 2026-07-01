# Expense Tracker

> OOP, file I/O, data structures

## Overview
A command-line expense tracker that lets you add, view, and summarize your expenses by category and month with persistent storage using a CSV file. Built with an OOP approach using an `Expense` class, then upgraded with Pandas for cleaner data analysis.

## Concepts Practiced
- OOP : `Expense` class with category, amount, date, and description
- File I/O :reading and writing CSV files
- Data manipulation with Pandas : `read_csv`, `to_csv`, `groupby`
- Summary methods : total by category, monthly summary
- Interactive menu with `input()` for user navigation

## How to Run
```bash
# from this folder
python main.py
```

## What I Learned
Before discovering Pandas, I was writing multiple nested loops just to calculate
the total expenses per category or group them by month, a lot of code for something
that should be simple. Switching to Pandas and using `groupby()` reduced all of that
to one line where I just specify the column to group by. That was the moment Pandas
clicked for me: it thinks about data the way you actually want to think about it,
not the way a loop does.

Working with CSV persistence also taught me the load → modify → save pattern properly.
Every operation : adding, removing, summarizing, starts by reading the full file into a DataFrame, doing the work in memory, then writing it back. Clean and predictable.

This project made me realize why data engineers reach for Pandas immediately instead
of raw loops. I'll be using it in every data-heavy project from here.

---
[← Back to main repo](../../README.md)