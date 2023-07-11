# Python - Input/Output

## Resources

## Read or watch

- [7.2. Reading and Writing Files](https://intranet.alxswe.com/rltoken/hFlrZ9E1XROVWcjwwyF52A)
- [8.7. Predefined Clean-up Actions](https://intranet.alxswe.com/rltoken/0OZ9fzPRjmKWZsID9IRJSg)
- [Dive Into Python 3: Chapter 11. Files (until “11.4 Binary Files” (included))](https://intranet.alxswe.com/rltoken/0osPfNU5d3Shh9PFWgYm9A)
- [JSON encoder and decoder](https://intranet.alxswe.com/rltoken/l0B9_pFn1tgBvE7FrT14Zw)
- [Learn to Program 8 : Reading / Writing Files](https://intranet.alxswe.com/rltoken/ZvtAdnUzjnEVu1sjg3m_tQ)
- [Automate the Boring Stuff with Python (ch. 8 p 180-183 and ch. 14 p 326-333)](https://intranet.alxswe.com/rltoken/Ej8YjhxLXpzHW7_rNMd9XQ)
- [All about py-file I/O](https://intranet.alxswe.com/rltoken/TUatlpPV27S4zPogmQIPnQ)

## Learning Objectives

At the end of this project, you are expected to be able to [explain to anyone](https://intranet.alxswe.com/rltoken/x2TxSf8LF65dpNOPSGtXgQ), without the help of Google:

## General

- Why Python programming is awesome
- How to open a file
- How to write text in a file
- How to read the full content of a file
- How to read a file line by line
- How to move the cursor in a file
- How to make sure a file is closed after using it
- What is and how to use the `with statement`
- What is `JSON`
- What is serialization
- What is deserialization
- How to convert a Python data structure to a JSON string
- How to convert a JSON string to a Python data structure

## Requirements

## Python Scripts

- Allowed editors: `vi, vim, emacs`
- All your files will be interpreted/compiled on `Ubuntu 20.04 LTS using python3 (version 3.8.5)`
- All your files should `end with a new line`
- The first line of all your files should be exactly `#!/usr/bin/python3`
- A `README.md` file, at the root of the folder of the project, is mandatory
- Your code should use the `pycodestyle (version 2.8.*)`
- All your files must be executable`chmod u+x *.py`
- The length of your files will be tested using `wc`

## Python Test Cases

- Allowed editors: `vi, vim, emacs`
- All your files should end with a `new line`
- All your test files should be inside a `folder tests`
- All your test files should be text files `(extension: .txt)`
- All your tests should be executed by using this command: `python3 -m doctest ./tests/*`
- All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
- All your classes should have a documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
- All your functions (inside and outside a class) should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`
- A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)
- We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Learning Outcome

For this project, I learned file handling in Python. I used the builtin `with`,
`open`, and `read` functions with the `json` module to read and write files and
serialization and deserialization of objects with JSON.

## Tests

- [tests](./tests): Folder for test files.

## Function Prototypes

Prototypes for functions written in this project:

| File                            |  Prototype                                                        |
| --------------------------------|-------------------------------------------------------------------|
| `0-read_file.py`                | `def read_file(filename=""):`
| `1-write_file.py`               | `def write_file(filename="", text=""):`
| `2-append_write.py`             | `def append_write(filename="", text=""):`
| `3-to_json_string.py`           | `def to_json_string(my_obj):`
| `4-from_json_string.py`         | `def from_json_string(my_str):`
| `5-save_to_json_file.py`        | `def save_to_json_file(my_obj, filename):`
| `6-load_from_json_file.py`      | `def load_from_json_file(filename):`
| `7-add_item.py`                 | `def add_item(args=[]):`
| `8-class_to_json.py`            | `def class_to_json(obj):`
| `9-student.py`                  | `def to_json(self):`
| `10-student.py`                 | `def to_json(self, attrs=None):`
| `11-student.py`                 | `def reload_from_json(self, json):`
| `12-pascal_triangle.py`         | `def pascal_triangle(n):`
| `100-append_after.py`           | `def append_after(filename="", search_string="", new_string=""):`
| `101-stats.py`                  | `def print_stats(text, status_codes):`

## Tasks

- **0. Read file**
  - [0-read_file.py](./0-read_file.py): Python function that prints the contents of a `UTF8` text
  file to standard output.
  - You must use the `with statement`.
  - No need to manage file permission or file doesn't exist exceptions.
  - No need to import any module

- **1. Write to a file**
  - [1-write_file.py](./1-write_file.py): Python function that writes a string to a UTF8 text
  file and returns the number of characters written.

- **2. Append to a file**
  - [2-append_write.py](./2-append_write.py): Python function that appends a string to the end of a
  UTF8 text file and returns the number of characters appended.

- **3. To JSON string**
  - [3-to_json_string.py](./3-to_json_string.py): Python function that returns the JSON string
  representation of an object.

- **4. From JSON string to Object**
  - [4-from_json_string.py](./4-from_json_string.py): Python function that returns the Python object
  represented by a JSON string.

- **5. Save Object to a file**
  - [5-save_to_json_file.py](./5-save_to_json_file.py): Python function that writes an object to a text
  file using JSON representation.

- **6. Create object from a JSON file**
  - [6-load_from_json_file.py](./6-load_from_json_file.py): Python function that creates an object from a
  `.json` file.
  - You must use the `with statement`.
  - No need to manage exceptions if the JSON string doesnt exit.
  - No need to manage file permissions or file doesn't exist exceptions.

- **7. Load, add, save**
  - [7-add_item.py](./7-add_item.py): Python script that stores all command line arguments to a
  Python list saved in the file `add_item.json`.
  - Use the function `save_to_json_file` from `5-save_to_json_file.py`
  - Use the function `load_from_json_file` from `6-load_from_json_file.py`
  - The list must be saved as a JSON representation in a file named `add_item.json`
  - Create file if it doesn’t exist.
  - No need to manage file permissions / exceptions.

- **8. Class to JSON**
  - [8-class_to_json.py](./8-class_to_json.py)
  - function returns the dictionary description with simple data structure (list, dictionary, string, integer and boolean) for JSON serialization of an object:
  - Prototype: `def class_to_json(obj):`
  - `obj` is an instance of a Class
  - All attributes of the `obj` Class are serializable: list, dictionary, string, integer and boolean
  - No need to import any module

- **9. Student to JSON**
  - [9-student.py](./9-student.py): Python class `Student` that defines a student. Includes:
    - Public instance attributes `first_name`, `last_name`, and `age`.
    - Instantiation with `first_name`, `last_name`, and `age`:
    `def __init__(self, first_name, last_name, age):`.
    - Public method `def to_json(self):` that returns the dictionary
    representation of a `Student` instance.
    - No need to import any module

- **10. Student to JSON with filter**
  - [10-student.py](./10-student.py): Python class `Student` that defines a student. Builds on
  [9-student.py](./9-student.py) with:
    - Public instance attributes `first_name`, `last_name`, and `age`.
    - Instantiation with `first_name`, `last_name`, and `age`:
    `def __init__(self, first_name, last_name, age):`.
    - Public method `def to_json(self, attrs=None):` that returns the
    dictionary representation of a `Student` instance.
      - If `attrs` is a list of strings, only the attributes listed are
    represented in the dictionary.
      - Otherwise, all attributes are retrieved.
    - No need to import any module

- **11. Student to disk and reload**
  - [11-student.py](./11-student.py): Python class `Student` that defines a student. Builds on
  [10-student.py](./10-student.py) with:
  - Public method `def to_json(self, attrs=None):` that retrieves a dictionary representation of a `Student` instance `(same as 8-class_to_json.py)`:
    - Public instance attributes `first_name`, `last_name`, and `age`.
    - Instantiation with `first_name`, `last_name`, and `age`: def `__init__(self, first_name, last_name, age):`.
      - If `attrs` is a list of strings, only the attributes listed are represented in the dictionary.
      - Otherwise, all attributes are retrieved.
  - Public method `def reload_from_json(self, json):` that replaces all attributes of the `Student` instance:
  - Assume json will always be a dictionary
  - A dictionary key will be the public attribute name
  - A dictionary value will be the value of the public attribute
  - No need to import any module

Now, you have a simple implementation of a serialization and deserialization mechanism (concept of representation of an object to another format, without losing any information and allow us to rebuild an object based on this representation)

- **12. Pascal's Triangle**
  - [12-pascal_triangle.py](./12-pascal_triangle.py): Python function that returns a list of lists of
  integers representing Pascal's triangle of size `n`.
  - Assumes the size parameter `n` is an integer.
  - If `n` is less than or equal to `0`, returns an empty list.

- **13. Search and update**
  - [100-append_after.py](./100-append_after.py): Python function that inserts a line of text to a
  file after each line containing a specified string.
  - Prototype: `def append_after(filename="", search_string="", new_string=""):`
  - Use the `with statement`
  - No need to manage `file permission` or `file doesn't exist` exceptions.
  - No need to import any module

- **14. Log parsing**
  - [101-stats.py](./101-stats.py): Python script that reads lines from standard input. After
  every 10 lines or the input of a keyboard interruption (`CTRL + C`), computes the
  following metrics:
    - Total file size up that point: `File size: <total size>`
    - Status code of each read line, printed in ascending order:
    `<status code>: <number>`
  - Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1"
  <status code> <file size>`
  - where is the sum of all previous (see input format above)
  - Number of lines by status code:
    - possible status code: 200, 301, 400, 401, 403, 404, 405 and 500
    - if a status code doesn’t appear, don’t print anything for this status code
    - format: <status code>: <number>
    - status codes should be printed in ascending order
