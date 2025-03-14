import streamlit as st
from backend import add_product 
st.set_page_config(layout="centered") 

st.header("Add Product")
product_name = st.text_input("Product Name")
description = st.text_area("Product Description")
price = st.number_input("Product Price $")
stock = st.number_input("Stock Quantity")
image = st.text_area("Product Image Link")
btn = st.button("Submit")
if btn:
    st.success("Product Added Sucessfully.")
    add_product( product_name, description, price, stock, image)

