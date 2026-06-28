# Password Strength Checker / Generator

> string manipulation, regex

## Overview
A command-line tool that checks the strength of any password and scores it as Weak, Medium, or Strong based on length, character variety, and complexity. It also generates secure passwords with customizable rules, length, uppercase, numbers, and special characters using named CLI flags.

## Concepts Practiced
- CLI argument handling with `sys.argv` and named flags
- Regular expressions with the `re` module
- String manipulation and `string` module constants
- Random selection and shuffling with the `random` module
- Boolean logic and point-based scoring
- Edge case handling, missing arguments, invalid values and length conflicts

## How to Run
```bash
#if you want to check your current password(use the following CLI)
python main.py
# If you want to generate a new password(use the following CLI)
python main.py generate --length 10 --uppercase  --numbers --special 
```

## What I Learned

Working with **Regular Expressions** using the `re` module was the main new concept here instead of looping through every character manually, one pattern like `[A-Z]` is enough to check the entire password instantly. That felt like a real upgrade in how I think about string problems.

For the generator, the trickiest part was the guaranteed characters logic randomly picking from the full pool isn't enough because you might get a password with no numbers even if the user asked for them. The fix was to pick one character from each required category first,
fill the rest randomly, then use `random.shuffle()` to mix everything so the guaranteed characters don't appear in an obvious position.

The CLI flag parsing with `sys.argv` also taught me how real tools like `git` or `pip`
handle named arguments, something I'll use in almost every project going forward.

---
[← Back to main repo](../../README.md)