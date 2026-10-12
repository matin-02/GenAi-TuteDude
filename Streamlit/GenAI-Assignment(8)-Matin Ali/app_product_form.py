# create a simple form UI:
# 1. Use Streamlit sidebar to enter:
# product name , category (selectbox 3 to 5 options) , price
import streamlit as st
st.title("Product Form App")
product_name = st.sidebar.text_input("Product Name")
Category = st.sidebar.selectbox("Select Category" , ["Electronics" , "Clothing" , "Home" , "Accessories"])
price = st.sidebar.number_input("Price " , min_value = 0.0)


if st.sidebar.button("Add Product"):
    st.success("Product Added Successfully !")
    st.write(f"Product Name : {product_name}")
    st.write(f"Category : {Category}")
    st.write(f"Price of Product is : {price}")