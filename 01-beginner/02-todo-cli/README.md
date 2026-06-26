# Command-line To-Do List

A terminal-based task manager that lets you add, list, complete, and remove
tasks directly from the command line with persistent storage using **JSON**.

## What it does

- Add tasks with a single command
- List all tasks with their status and date added
- Mark tasks as done
- Remove tasks by number
- Saves everything to a local JSON file — tasks persist between sessions

## Concepts Practiced

- CLI argument handling with `sys.argv`
- File I/O, reading and writing JSON
- Error handling, missing files, missing arguments
- Working with dates using the `datetime` module
- Dictionary and list manipulation



## How to Run
```bash
python main.py add "Buy milk"
python main.py list
python main.py done "1"
python main.py remove "1"
```

## What I Learned

Building this taught me how `sys.argv` turns terminal input into a list Python can actually read — once that clicked, handling commands like `add` or `remove` felt natural. The trickiest part was JSON persistence: understanding that you have to load the full file, modify it in memory, then write the entire thing back, not just append to it. I also learned to always handle the case wherev the file doesn't exist yet, otherwise the program crashes on the very first run.

---
[← Back to main repo](../../README.md)
