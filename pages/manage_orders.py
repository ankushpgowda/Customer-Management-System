import streamlit as st
from streamlit_option_menu import option_menu
from backend import get_orders, get_customer_firstname, get_order_details, modify_status
st.set_page_config(layout="wide")

with st.sidebar:
    st.title(f"Welcome :red[Admin] !")
    st.markdown(" ")
    st.session_state.selected = option_menu(
        menu_title=None,
        options=["Manage Customers", "Manage Products", "Manage Orders"],
        icons=["person-fill-gear", "pc-display", "truck"],
        default_index=2
    )
    st.page_link("pages/login.py", label="Logout")

st.title("Orders")
with st.container(border=True):
    col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 2, 1, 1, 1])
    col1.write(f"Order ID:")
    col2.write(f"Customer First Name:")
    col3.write(f"Order Details :")
    col4.write(f"Total Paid:")
    col5.write(f"Order Status:")
    col6.write(f"Action:")

orders = get_orders()
for order in orders:
    with st.container(border=True):
        col1, col2, col3, col4, col5, col6 = st.columns([1, 1, 2, 1, 1, 1])
        col1.write(f"{order[0]}")
        col2.write(f"{get_customer_firstname(order[1])}")
        col3.write(f"{get_order_details(order[0])}")
        col4.write(f"$ {order[3]}")
        col5.write(f"{order[4]}")
        with col6.container():
            
            col6_1 = st.container()
            if col6_1.button('Delivered', key=f"delivered_{order[0]}"):
                modify_status("Delivered", order[0])
                st.rerun()
            
            col6_2 = st.container()
            if col6_2.button('Cancel', key=f"cancel_{order[0]}"):
                modify_status("Cancelled and Refund Issued", order[0])
                st.rerun()

            col6_3 = st.container()
            if col6_2.button('Refunded', key=f"refunded_{order[0]}"):
                modify_status("Refunded", order[0])
                st.rerun()


if st.session_state.selected == "Manage Customers":
    st.switch_page("pages/a_dashboard.py")
elif st.session_state.selected == "Manage Products":
    st.switch_page("pages/manage_products.py")