# Password Strength Checker / Generator

> string manipulation, regex

## Overview
A command-line tool that checks the strength of any password and scores it as Weak, Medium, or Strong based on length, character variety, and complexity. It also generates secure passwords with customizable rules — length, uppercase, numbers, and special characters — using named CLI flags.

## Concepts Practiced
- CLI argument handling with `sys.argv` and named flags
- Regular expressions with the `re` module
- String manipulation and `string` module constants
- Random selection and shuffling with the `random` module
- Boolean logic and point-based scoring
- Edge case handling — missing arguments, invalid values, length conflicts

## How to Run
```bash
# from this folder
python main.py generate --length 16 --uppercase yes --numbers yes --special yes
```

## What I Learned


---
[← Back to main repo](../../README.md)