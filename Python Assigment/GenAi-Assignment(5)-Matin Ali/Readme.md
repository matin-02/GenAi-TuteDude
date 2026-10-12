Assignment 5: Importing, Creating Modules & Packages
Description

This assignment demonstrates how to create Python modules, import modules, and organize modules into a package.

The assignment focuses on:

Creating Python modules
Importing modules using import
Importing functions using from ... import
Creating and using Python packages
Using __init__.py
Keeping the code simple and beginner-friendly
Folder Structure
modules_assignment/
│
├── main.py
├── math_utils.py
├── string_utils.py
│
└── shop_package/
    ├── __init__.py
    ├── discount.py
    └── billing.py
Files Description
math_utils.py

Contains basic mathematical functions:

add(a, b) - Adds two numbers
subtract(a, b) - Subtracts two numbers
square(n) - Returns the square of a number
string_utils.py

Contains basic string functions:

capitalize_words(text) - Capitalizes each word
reverse_string(text) - Reverses a string
word_count(text) - Counts the number of words
shop_package

A package containing two modules.

discount.py

Contains:

apply_discount(price, percent) - Applies a percentage discount
flat_discount(price) - Subtracts 50 from the price
billing.py

Contains:

calculate_total(prices) - Calculates the total of all prices
apply_tax(amount) - Adds 5% tax
init.py

Used to initialize the shop_package package and can expose functions from its modules.

How to Run
Open the project folder in a terminal or VS Code.
Make sure Python is installed.
Run the following command:
python main.py
Concepts Used
Python Modules
Python Packages
import module
from module import function
__init__.py
Functions
Restrictions

This assignment does not use:

OOP
Classes
Exceptions
File handling
External libraries

The code is kept simple to focus on understanding modules and packages.