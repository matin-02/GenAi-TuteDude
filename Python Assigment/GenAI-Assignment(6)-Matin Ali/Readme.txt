# Assignment 6: Exception Handling

## Problem Statement

This assignment focuses on handling unexpected user inputs, invalid operations, and runtime errors using Python exception handling.

The assignment covers try, except, multiple except blocks, else, finally, and raise.

## Task 1: Safe Division Utility

This task performs division using two numbers entered by the user.

It handles ValueError and ZeroDivisionError and uses else to display the result and finally to display Operation Complete.

## Task 2: Bill Calculator with Error Handling

This task processes a list of product prices.

It adds only valid positive numerical prices to the total. It handles TypeError for non-numeric values and raises ValueError for negative prices.

Invalid items are skipped and processing continues.

## Task 3: Custom Exception: Age Validator

This task validates the age entered by the user.

The check_age function raises ValueError when the age is not between 1 and 120.

The error is handled using try and except.

## Task 4: File Reader with Exception Handling

This task asks the user for a filename and attempts to read the file.

It handles FileNotFoundError and PermissionError.

If the file is successfully opened, the first three lines are displayed.

The finally block displays File Operation Attempted.

## Task 5: Mini Program: Safe Shopping Cart

This task creates a simple shopping cart program.

The program allows the user to enter product prices and stops when q is entered.

It converts the input to float, handles ValueError for invalid input, and raises ValueError for negative prices.

At the end, it displays the total number of items and the total bill.

## How to Run the Programs

1. Open the assignment folder in VS Code or another Python editor.
2. Open the Python file containing the task you want to run.
3. Run the program.
4. Enter the required input when prompted.
5. Check the output in the terminal or output window.
6. Run each task separately to test the exception handling.

For Task 4, make sure the file you enter exists and is accessible.

## Concepts Used

* try
* except
* Multiple except blocks
* else
* finally
* raise
* ValueError
* TypeError
* ZeroDivisionError
* FileNotFoundError
* PermissionError
* Lists
* Loops
* User input

## Conclusion

This assignment provides practical experience with Python exception handling. It helps create simple and safe programs that can handle invalid inputs and runtime errors without stopping unexpectedly.
