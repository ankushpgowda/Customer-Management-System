import streamlit as st
from streamlit_option_menu import option_menu
from backend import get_customer_order, get_order_details
st.set_page_config(layout="wide")

with st.sidebar:
    st.title(f"Welcome :red[{st.session_state.firstname}] !")
    st.markdown(" ")
    st.session_state.selected = option_menu(
        menu_title=None,
        options=["Store", "Basket", "Order's History"],
        icons=["shop", "basket", "hourglass"],
        default_index=2
    )
    st.page_link("pages/login.py", label="Logout")

st.title("Orders History")
with st.container(border=True):
    col1, col2, col3 = st.columns([2, 1, 1])
    col1.write(f"Order Details :")
    col2.write(f"Total Paid:")
    col3.write(f"Order Status:")

orders = get_customer_order()
for order in orders:
    with st.container(border=True):
        col1, col2, col3 = st.columns([2, 1, 1])
        col1.write(f"{get_order_details(order[0])}")
        col2.write(f"$ {order[3]}")
        col3.write(f"{order[4]}")

if st.session_state.selected == "Basket":
    st.switch_page("pages/basket.py")
elif st.session_state.selected == "Order's History":
    st.switch_page("pages/history.py")