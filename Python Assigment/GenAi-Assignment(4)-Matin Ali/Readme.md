Assignment 4 - File Handling

## Description

This assignment covers basic file handling in Python.

The following file operations are used:

* Read a file
* Write to a file
* Append to a file
* Read using 'read()'
* Read using 'readline()'
* Read using 'readlines()'
* Check if a file exists
* Work with files using 'with open()'

## Tasks

### Task 1 - Sales Records

* Create a list of sales.
* Write the sales into 'sales_data.txt'.
* Read the file and print the contents.

### Task 2 - Read File

Read 'sales_data.txt' using:

* 'read()'
* 'readline()'
* 'readlines()'

Convert the sales values into integers.

### Task 3 - Append New Sales Record

* Open 'sales_data.txt' in append mode ('a').
* Add a new sales record to the existing file.
* Read the file again.
* Print all the sales records.

This task demonstrates how to add new data without deleting the existing data.

### Task 4 - Sales Summary

Read the sales from the file and calculate:

* Total Sales
* Highest Sale
* Lowest Sale
* Average Sale

### Task 5 - Product Information

* Ask the user for 3 product names and prices.
* Save them in 'products.txt'.
* Read and print the file contents.

### Task 6 - Safe File Reading

* Ask the user for a filename.
* Check if the file exists using 'os.path.exists()'.
* If the file exists, read and print it.
* If it does not exist, display an error message.

### Task 7 - Discount Report

* Create a dictionary of product prices.
* Ask the user for a discount percentage.
* Calculate discounted prices.
* Save the results in 'discount_report.txt'.
* Read and print the report.
* Calculate the total number of items and average discounted price.

## Files Used

text
sales_data.txt
products.txt
discount_report.txt


## Requirements

* Python 3
* No pandas
* No csv module
* No external libraries
* Use basic Python file handling
* Use 'with open()' for file operations

## How to Run

1. Install Python 3.
2. Open the project folder.
3. Run the Python program.
4. Follow the instructions shown in the terminal.

Example:
bash
python assignment4.py

## Concepts Learned

* File opening modes: 'r', 'w', 'a', 'r+', 'w+'
* Reading files
* Writing files
* Appending files
* Converting text to integers
* Basic calculations
* Checking file existence
* Safe file handling with 'with open()'
