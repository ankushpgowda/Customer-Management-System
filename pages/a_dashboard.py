import streamlit as st
from streamlit_option_menu import option_menu
from backend import get_customers, delete_customer
st.set_page_config(layout="wide")

with st.sidebar:
    st.title(f"Welcome :red[Admin] !")
    st.markdown(" ")
    st.session_state.selected = option_menu(
        menu_title=None,
        options=["Manage Customers", "Manage Products", "Manage Orders"],
        icons=["person-fill-gear", "pc-display", "truck"],
        default_index=0
    )
    st.page_link("pages/login.py", label="Logout")

st.title("Customers")
with st.container(border=True):
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.write(f"First Name:")
    col2.write(f"Last Name:")
    col3.write(f"Email:")
    col4.write(f"Phone Number:")
    col5.write(f"Address:")
    col6.write(f"Action:")

customers = get_customers()
for customer in customers:
    with st.container(border=True):
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        col1.write(f"{customer[1]}")
        col2.write(f"{customer[2]}")
        col3.write(f"{customer[3]}")
        col4.write(f"{customer[5]}")
        col5.write(f"{customer[6]}")
        with col6.container():
            
            col6_1 = st.container()
            if col6_1.button('Edit', key=f"edit_{customer[0]}"):
                st.session_state.edit_data = customer
                st.switch_page("pages/edit_form.py")
            
            col6_2 = st.container()
            if col6_2.button('Delete', key=f"approve_{customer[0]}"):
                delete_customer(customer[0])
                st.rerun()

if st.session_state.selected == "Manage Products":
    st.switch_page("pages/manage_products.py")
elif st.session_state.selected == "Manage Orders":
    st.switch_page("pages/manage_orders.py")