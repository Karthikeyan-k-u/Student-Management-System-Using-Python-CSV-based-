# Student-Management-System-Using-Python-CSV-based-

## Description
A console-based Student Management System written in Python that stores student data in a CSV file.   The program allows users to add, view, update, and delete student records. Data persists between sessions because it's saved to a CSV file. It uses Python's built-in `csv` module and file handling operations.

## Features
- **Add Student** – Insert a new student record (ID, Name, Department, Marks).
- **View All Students** – Display all stored student records.
- **Update Student** – Modify an existing student record by ID.
- **Delete Student** – Remove a student record by ID.
- **CSV Persistence** – Data is automatically saved to a CSV file and reloaded when the program starts.
- **File Initialization** – Creates the CSV file with headers if it doesn’t exist.

---

## Algorithm

### 1. File Handling
- File path: `C:\Users\karth\OneDrive\csvproject.csv` (hardcoded – can be adjusted).
- `init_file()`: Checks if file exists; if not, creates it with headers `["ID", "Name", "Dept", "Marks"]`.

### 2. Data Operations
- `read_data()`: Opens the CSV file, reads all rows using `csv.DictReader`, and returns a list of dictionaries.
- `write_data(data)`: Writes the provided list of dictionaries to the CSV file with headers.

### 3. CRUD Functions
- `add_student()`:
  - Prompts for ID, Name, Department, Marks.
  - Appends the new dictionary to the existing data.
  - Writes back to the file.
- `view_students()`:
  - Reads data and prints each record.
- `update_student()`:
  - Reads data, searches for matching ID.
  - If found, prompts for new values for all fields.
  - Writes updated list back to file.
- `delete_student()`:
  - Reads data, filters out the record with the given ID.
  - Writes the filtered list back.

### 4. Main Menu Loop (`menu()`)
- Calls `init_file()` to ensure CSV exists.
- Displays menu options:
  1. Add
  2. View
  3. Update
  4. Delete
  5. Exit
- Repeats until user chooses exit.
