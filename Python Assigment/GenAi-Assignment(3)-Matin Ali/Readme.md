# Assignment 3 – Python Functions

## Description

This assignment focuses on Python functions and different ways of using them. The programs demonstrate user-defined functions, recursive functions, lambda functions, `map()`, `filter()`, default arguments, and combining these concepts.

## Topics Covered

* User-defined functions
* Default arguments
* Recursive functions
* Lambda functions
* `map()`
* `filter()`
* Loops
* Function calls

## Tasks

### Task 1 – Basic Function: Price After Discount

Created a function `apply_discount()` that calculates the price after applying a discount.

* Uses a default discount of 5%.
* Supports a user-provided discount.
* Optional maximum discount of 60%.

### Task 2 – Recursive Function: Factorial Utility

Created a recursive function `factorial()` that calculates the factorial of a number.

* Handles `0` and `1`.
* Displays an error message for negative numbers.
* Demonstrates recursion.

### Task 3 – Lambda Function: GST Calculator

Created a lambda function `gst` that adds 18% GST to a price.

Example:

```python
gst = lambda price: price + (0.18 * price)

print(gst(100))
```

### Task 4 – Using `map()`

Used `map()` with a lambda function to apply 18% GST to a list of prices.

### Task 5 – Using `filter()`

Used `filter()` to separate prices into:

* Prices greater than 500
* Prices less than or equal to 500

### Task 6 – Combined Utility Function

Created `process_prices()` that:

1. Applies a 10% discount using `map()`.
2. Uses `filter()` to keep prices above 300.
3. Returns both the discounted and filtered lists.

### Task 7 – Menu Using Functions

Created a simple menu program using functions and a loop.

Menu options:

```text
1 → Add price
2 → Show average price
3 → Show highest price
q → Quit
```

Functions used:

* `add_price()`
* `get_average_price()`
* `get_max_price()`

## Restrictions Followed

This assignment does not use:

* Classes / OOP
* External packages
* Exceptions
* File handling

The programs use basic Python concepts and are kept simple and readable.

## How to Run

1. Open the Python files or Jupyter Notebook cells.
2. Run each task separately.
3. Follow the instructions displayed by the programs.
4. For Task 7, enter the menu option to perform the required operation.

## Requirements

* Python 3.x
* No external libraries are required.

## Conclusion

This assignment provides practice with Python functions and functional programming features such as recursion, lambda functions, `map()`, and `filter()`.
