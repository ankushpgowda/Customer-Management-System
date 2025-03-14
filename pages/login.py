import streamlit as st
from backend import login_checker, admin_checker
st.set_page_config(layout="centered") 

st.header("Login")
email = st.text_input("Enter your Email")
password = st.text_input("Enter your password", type="password")
btn = st.button("Submit")
if btn:
    if admin_checker(email, password):
        st.switch_page("pages/a_dashboard.py")
    else:
        email, password = login_checker(email, password)
        if email and password: 
            st.success("Login Successful")
            st.switch_page("pages/s_dashboard.py")
        elif email or password:
            st.error("Check your Email or Password")
        else:
            st.error("New User? Create a Account.")
st.page_link("pages/signup.py", label="Dont have account. New Customer?")

    

