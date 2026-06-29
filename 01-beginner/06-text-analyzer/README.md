# Text Analyzer

> string processing, dictionaries, file I/O

## Overview
A command-line tool that reads any text file and outputs a full analysis, word frequency, sentence count, average word length, and the top 10 most common words. Built as a warm-up for NLP preprocessing concepts used later in machine learning projects.
 
## Concepts Practiced
- File I/O : reading raw text from a file
- String processing : cleaning, stripping punctuation, lowercasing
- Regular expressions with `re` splitting on sentence endings
- Dictionaries : building and sorting a word frequency counter


## How to Run
```bash
# from this folder
python main.py
```

## What I Learned

This project taught me how important text cleaning is before any analysis stripping punctuation using `string.punctuation` and lowercasing with `.lower()` made the difference between getting "The" and "the" counted as two different words or one. A small step that matters a lot in real NLP work.

I also discovered the `Counter` class from the `collections` module, which made
counting word frequency and finding the top 10 most common words much cleaner
than building a manual dictionary loop. It's a tool I'll keep using.

The trickiest bug was using `splitlines()` instead of reading the file as one string first, it gave me 12 "sentences" instead of 9 because it was splitting on line breaks, not punctuation. Fixing that taught me to always think about the shape of my data before processing it.

---
[← Back to main repo](../../README.md)
