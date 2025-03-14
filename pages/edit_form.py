import streamlit as st
from backend import edit_details
st.set_page_config(layout="centered")

st.header("Edit Form")
first_name = st.text_input("First Name", value=st.session_state.edit_data[1])
last_name = st.text_input("Last Name", value=st.session_state.edit_data[2])
email = st.text_input("Email", value=st.session_state.edit_data[3])
number = st.text_input("Phone Number", value=st.session_state.edit_data[5])
address = st.text_area("Address", value=st.session_state.edit_data[6])
btn = st.button("Submit")
if btn:
    st.success("Account Edited Sucessfully. Please Login")
    edit_details(st.session_state.edit_data[0], first_name, last_name, email, number, address)
    