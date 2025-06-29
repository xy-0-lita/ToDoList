# ToDoList
# ToDo List Manager

A simple command-line ToDo list application built in Python as part of my learning journey with Mimo.

## Features

- Add tasks to your ToDo list
- Remove the most recently added task
- Display your current ToDo list
- Simple menu-driven interface
- Session-based (list resets when program restarts)

## Usage

1. Run the program:
   ```
   python todo.py
   ```

2. Choose from the menu options:
   - **1** - Add a new task
   - **2** - Remove the last added task
   - **3** - Display your current list
   - **4** - Quit the program

3. Follow the prompts to manage your tasks!

## Example
```
Options:
1) Add Task
2) Remove Task
3) Display List
4) Quit
Choose option (1, 2, 3, or 4): 1
Adding task
Enter the task you want to add: Buy groceries
Task is added to list
Current ToDo list: 
- Buy groceries
```

## What I Learned

Building this project helped me practice several key Python concepts:
- **Functions**: Creating reusable code with `display_list()`
- **Lists**: Using `append()` and `pop()` methods for data management
- **Control Flow**: Implementing `while` loops and `if/elif/else` statements
- **User Input**: Handling user interaction with `input()`
- **String Formatting**: Using f-strings for clean output

## Future Features

- Allow users to insert tasks at specific positions
- Enable removal of specific tasks (not just the last one)
- Add task priorities or categories
- Save tasks between sessions
- Add due dates for tasks

## Acknowledgments

Built while learning Python through [Mimo](https://mimo.org) - thanks for the great learning platform!

---

*This is my first project shared on GitHub as part of my coding learning journey!*
