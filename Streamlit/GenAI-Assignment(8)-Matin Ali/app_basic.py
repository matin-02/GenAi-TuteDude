# Create a basic Streamlit app that 
# display a title : "Welcome to Streamlit"
import streamlit as st
st.title("Welcome to Streamlit")

# Show  a text input box for entering your name
name = st.text_input("Enter Your Name : ")

# when the user click a button "Greet Me" , display " Hello, !"
if st.button("Greet Me"):
    st.write(f"Hello, {name} !")