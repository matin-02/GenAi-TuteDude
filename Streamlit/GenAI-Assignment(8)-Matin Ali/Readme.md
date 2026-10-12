# Assignment 8: Streamlit Basic App Building

## Introduction

This assignment focuses on creating simple and interactive web applications using Streamlit.

The applications use basic Streamlit components such as text input, number input, slider, button, selectbox, sidebar, success message, table, metric, and bar chart.

The assignment is designed to practice beginner-friendly Streamlit concepts.

## Folder Structure

streamlit assignment/

* app_basic.py
* app_discount.py
* app_product_form.py
* app_dashboard.py

## Task 1: Basic Streamlit App

File: app_basic.py

This task creates a basic Streamlit application.

The application:

* Displays the title Welcome to Streamlit!
* Takes the users name using a text input
* Provides a Greet Me button
* Displays a greeting message after clicking the button

## Task 2: Price Calculator

File: app_discount.py

This task creates a simple price calculator.

The application:

* Takes the product price using a number input
* Takes the discount percentage using a slider from 0 to 50 percent
* Calculates the discounted price
* Displays the final price using a success message
* Displays a comparison table showing the price before and after discount

## Task 3: Product Form

File: app_product_form.py

This task creates a simple product form using the Streamlit sidebar.

The application:

* Takes the product name using a sidebar text input
* Allows the user to select a category using a sidebar selectbox
* Takes the product price using a sidebar number input
* Provides an Add Product button
* Displays a success message
* Displays the entered product details

## Task 4: Mini Dashboard

File: app_dashboard.py

This task creates a simple sales dashboard.

The application:

* Displays the title Simple Sales Dashboard
* Displays a description about monthly sales
* Provides a selectbox for selecting a month
* Stores monthly sales in a static dictionary
* Displays the selected months sales
* Displays monthly sales using a bar chart

## Streamlit Components Used

The following Streamlit components are used in this assignment:

* st.title
* st.write
* st.text_input
* st.number_input
* st.slider
* st.button
* st.sidebar
* st.sidebar.text_input
* st.sidebar.selectbox
* st.sidebar.number_input
* st.sidebar.button
* st.success
* st.table
* st.selectbox
* st.metric
* st.subheader
* st.bar_chart

## How to Run

First, install Streamlit if it is not already installed.

Then open the terminal in the assignment folder.

Run each application separately using the Streamlit command.

Task 1:

streamlit run app_basic.py

Task 2:

streamlit run app_discount.py

Task 3:

streamlit run app_product_form.py

Task 4:

streamlit run app_dashboard.py

## Conclusion

This assignment provides basic practice with Streamlit and demonstrates how to create simple interactive applications using user inputs, buttons, selections, calculations, and visual displays.
