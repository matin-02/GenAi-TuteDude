# Assignment 7: Object-Oriented Programming (OOP)

## Problem Statement

This assignment focuses on the basic concepts of Object-Oriented Programming in Python.

The assignment covers classes, objects, constructors, encapsulation, inheritance, polymorphism, abstraction, magic methods, and operator overloading.

## Tasks Completed

### Task 1: Basic Class and Object Creation

Created a Product class with name, price, and category attributes.

Created the get_info() method to display product details.

Created two Product objects and displayed their information.

### Task 2: Constructor and Encapsulation

Used the __init__() constructor to initialize product details.

Made the price attribute private.

Created getter and setter methods to access and update the price.

The setter updates the price only when the new price is greater than 0.

### Task 3: Inheritance

Created an ElectronicProduct class that inherits from the Product class.

Added warranty_years as an additional attribute.

Overrode the get_info() method to display warranty information.

### Task 4: Polymorphism

Created Laptop and Mobile classes that inherit from Product.

Both classes override the get_info() method.

Used a loop to call get_info() for different objects.

### Task 5: Abstraction

Created an abstract Payment class.

Created CreditCardPayment and UPIPayment classes.

Both classes implement the process_payment() method.

### Task 6: Magic Methods and Operator Overloading

Added the __str__() magic method to display product information in a readable format.

Added the __add__() method to combine the prices of two Product objects.

### Task 7: Simple Inventory System

Created Product, Inventory, and Store classes.

The Inventory class stores Product objects in a list.

Implemented methods to add products, remove products, calculate total inventory value, and display all products.

The Store class manages the store name and Inventory object.

Added user input for creating new products.

Used a loop to add multiple products.

Displayed the total number of products and total inventory value.

Used operator overloading to combine the prices of two products.

## OOP Concepts Used

* Classes and Objects
* Constructors
* Attributes and Methods
* Encapsulation
* Inheritance
* Polymorphism
* Abstraction
* Magic Methods
* Operator Overloading

## Restrictions Followed

* No file handling
* No external packages
* No advanced OOP patterns
* No exception handling
* Simple and beginner-friendly Python code

## How to Run the Program

1. Open the Python program in VS Code or Jupyter Notebook.
2. Run the program.
3. Enter the required product details when prompted.
4. The program displays all products and the inventory summary.
5. The program also displays the combined price of two products.

## Conclusion

This assignment demonstrates the basic Object-Oriented Programming concepts in Python through a simple electronics store and inventory system.
