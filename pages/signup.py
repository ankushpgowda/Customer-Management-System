import streamlit as st
from backend import add_details 
st.set_page_config(layout="centered") 

st.header("Sign Up")
first_name = st.text_input("First Name")
last_name = st.text_input("Last Name")
email = st.text_input("Email")
cr_password = st.text_input("Create Password", type="password")
co_password = st.text_input("Confirm Password", type="password")
number = st.text_input("Phone Number")
address = st.text_area("Address")
btn = st.button("Submit")
if btn:
    print(address)
    if cr_password == co_password:
        st.success("Account Created Sucessfully. Please Login")
        add_details(first_name, last_name, email, co_password, number, address)
st.page_link("pages/login.py", label="Back to login")

