# Build a simple price calculator app that
import streamlit as st
st.title("Price Calculator App")

# takes product price(number input)
price = st.number_input("Enter the price of the product : ")

# take a discount percentages(silder from 0 to 50%)
discount = st.slider("Select Discount(%)", 0, 50 , 0)

# on clicking the button "calculate the discounted price"
if st.button("Calculate Discounted Price"):
    discounted_price = price * discount / 100

    final_price = price - discounted_price

    st.success("Discounted Price : " + str(final_price))


# Extra(Optional) : Comparsion between original price and discounted price

    comparison = [
            ["Before" , "After Discount"] ,
            [price , final_price]
                ]
    st.table(comparison)
