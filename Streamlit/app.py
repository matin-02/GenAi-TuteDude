import pandas as pd
import streamlit as st

st.write("Hello,world")
st.title("My First Streamlit App")

st.header("This is a header")
st.subheader("This is a subheader")
st.text("this is a plain text")
agree = st.checkbox("I agree")
if agree:
    st.write("you agreed")


level = st.slider("select a Level : " , 1, 10 , 5)
st.write("selected level is : " , level)

uploaded_file = st.file_uploader("Upload a file",type = ["csv" , "txt"])

if uploaded_file is not None:
    df = pd.read_csv(uploaded_file)
    st.write(df.head())
