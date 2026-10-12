# Create a small dashboard with:
# 1. title + description
import streamlit as st
st.title("Simple Sales Dashboard")
st.write("The Dashboard Shows Monthly Sales")

# 2. A selectboc with months
months = ["January" , "February" , "March" , "April"]

# select a month
selected_month = st.selectbox("Select a Month" , months)

# 3. Static dictionary of monthly sales:
sales = {
    "January" : 1200 ,
    "February" : 1500 ,
    "March" : 900,
    "April" : 2000
}

# 4. Display selected month's sales using :
# st.metric or st.write()
st.metric("Sales : ", sales[selected_month])

# 5. display a bar chart using:
# st.bar_chart()
st.subheader("Monthly Sales")
st.bar_chart(sales)