import streamlit as st
from streamlit_option_menu import option_menu
from backend import get_total_price, get_basket, delete_item, checkout_basket
st.set_page_config(layout="wide")

with st.sidebar:
    st.title(f"Welcome :red[{st.session_state.firstname}] !")
    st.markdown(" ")
    st.session_state.selected = option_menu(
        menu_title=None,
        options=["Store", "Basket", "Order's History"],
        icons=["shop", "basket", "hourglass"],
        default_index=1
    )
    st.page_link("pages/login.py", label="Logout")

st.title("Your Basket")
if st.button("Pay", key=f"Pay"):
    checkout_basket()
    st.success("Your order is sucessfully placed")
st.header(f"Total Price: ${get_total_price()}")
with st.container(border=True):
    col1, col2, col3, col4, col5 = st.columns(5)
    col1.write(f"Products:")
    col2.write(f"Product Name:")
    col3.write(f"Units:")
    col4.write(f"Unit Price:")
    col5.write(f"Action:")

items = get_basket()
for item in items:
    with st.container(border=True):
        col1, col2, col3, col4, col5 = st.columns(5)
        col1.image(f"{item[0]}")
        col2.write(f"{item[1]}")
        col3.write(f"{item[3]}")
        col4.write(f"{item[2]}")
        with col5.container():
            col5_1 = st.container()
            if col5_1.button('Delete', key=f"delete_{item[0]}"):
                delete_item(item[4])
                st.rerun()


if st.session_state.selected == "Store":
    st.switch_page("pages/s_dashboard.py")
elif st.session_state.selected == "Order's History":
    st.switch_page("pages/history.py")