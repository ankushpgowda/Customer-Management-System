import streamlit as st
from backend import edit_product_details
st.set_page_config(layout="centered")

st.header("Edit Form")
product_name = st.text_input("Product Name", value=st.session_state.edit_product_data[1])
description = st.text_area("Product Description", value=st.session_state.edit_product_data[2])
price = st.number_input("Product Price $", value=float(st.session_state.edit_product_data[3]))
stock = st.number_input("Stock Quantity", value=int(st.session_state.edit_product_data[4]))
image = st.text_area("Product Image Link", value=st.session_state.edit_product_data[5])
btn = st.button("Submit")
if btn:
    st.success("Account Edited Sucessfully. Please Login")
    edit_product_details(st.session_state.edit_product_data[0], product_name, description, price, stock, image)
    