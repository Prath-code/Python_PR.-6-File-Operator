# File Operator: Personal Journal Manager

## Overview
The File Operator project is a Python application that allows users to maintain a personal journal using text file handling. Users can add, view, search, and delete journal entries, with robust exception handling and a menu-driven interface. The project demonstrates Object-Oriented Programming (OOP) principles and proper file handling techniques.

## Features
- Add new journal entries (with timestamp and user input)
- View all journal entries
- Search for entries by keyword or date
- Delete all journal entries (with confirmation)
- Exception handling for file errors and invalid input
- Menu-driven user interface

## Learning Objectives
- Understand and implement file handling operations (read, write, append, etc.)
- Use different file modes (`r`, `w`, `a`, `x`) and explain their impact
- Perform I/O operations (reading from and writing to files)
- Handle exceptions such as `FileNotFoundError`, `PermissionError`, and others
- Apply OOP principles to structure the application

## Project Requirements
- Operate only on text files (`.txt`)
- Store journal entries in a file named `journal.txt`
- Each entry must include a timestamp and user input
- Display clear error messages and guidance for invalid actions

## Usage
1. **Add a New Entry:**
   - Users can write a new journal entry. The program appends the entry to `journal.txt`, creating the file if it does not exist.
2. **View All Entries:**
   - Display all journal entries from the file. If the file does not exist, prompt the user to add a new entry.
3. **Search for an Entry:**
   - Search for entries by keyword or date and display matching entries.
4. **Delete All Entries:**
   - Clear the journal by deleting the file. Prompt the user for confirmation before deleting.
5. **Exit:**
   - Exit the program from the main menu.

## Example Console Interaction
```
Welcome to Personal Journal Manager!
Please select an option:
1. Add a New Entry
2. View All Entries
3. Search for an Entry
4. Delete All Entries
5. Exit
```

**Add a New Entry:**
```
Enter your journal entry:
Today was a productive day. I learned about file handling in Python.
Entry added successfully!
```

**View All Entries:**
```
Your Journal Entries:
-----------------------------
[2024-12-25 18:00:00]
Today was a productive day. I learned about file handling in Python.

[2024-12-24 18:00:00]
Had a great session on OOP concepts!
```

**Search for an Entry:**
```
Enter a keyword or date to search: productive
Matching Entries:
-----------------------------
[2024-12-25 18:00:00]
Today was a productive day. I learned about file handling in Python.
```

**Delete All Entries:**
```
Are you sure you want to delete all entries? (yes/no): yes
All journal entries have been deleted.
```

**Handle File Not Found Error:**
```
Error: The journal file does not exist. Please add a new entry first.
```

**Invalid Input:**
```
Invalid option. Please select a valid option from the menu.
```

**Exit:**
```
Thank you for using Personal Journal Manager. Goodbye!
```

## Exception Handling
- Handles exceptions for invalid file operations (e.g., missing file, permission errors)
- Ensures the program does not crash due to unexpected user input or file handling issues
- Provides clear error messages and guidance

## OOP Structure
- All functionality is encapsulated in a `JournalManager` class
- Uses instance methods for adding, reading, searching, and deleting entries

## Assumptions
- Only text files are used for journal storage
- Journal entries are stored in `journal.txt` in the project directory
- The user interacts with the program via the console
- The program is intended for educational purposes and demonstrates OOP and file handling in Python

## How to Run
1. Ensure you have Python 3.x installed.
2. Run the program:
   ```
   python project-6.py
   ```
3. Follow the on-screen menu instructions.

---

**Quality is our Motto.**
