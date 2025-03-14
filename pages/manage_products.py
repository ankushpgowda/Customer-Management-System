import streamlit as st
from streamlit_option_menu import option_menu
from backend import get_products, delete_product
st.set_page_config(layout="wide")

with st.sidebar:
    st.title(f"Welcome :red[Admin] !")
    st.markdown(" ")
    st.session_state.selected = option_menu(
        menu_title=None,
        options=["Manage Customers", "Manage Products", "Manage Orders"],
        icons=["person-fill-gear", "pc-display", "truck"],
        default_index=1
    )
    st.page_link("pages/login.py", label="Logout")

st.title("Products")
with st.container(border=True):
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.write(f"Product:")
    col2.write(f"Product Name:")
    col3.write(f"Description:")
    col4.write(f"Price:")
    col5.write(f"Stock Quantity:")
    col6.write(f"Action:")

products = get_products()
for product in products:
    with st.container(border=True):
        col1, col2, col3, col4, col5, col6 = st.columns(6)
        col1.image(f"{product[5]}", use_container_width=True)
        col2.write(f"{product[1]}")
        col3.write(f"{product[2]}")
        col4.write(f"$ {product[3]}")
        col5.write(f"{product[4]}")
        with col6.container():
            
            col6_1 = st.container()
            if col6_1.button('Edit', key=f"edit_{product[0]}"):
                st.session_state.edit_product_data = product
                st.switch_page("pages/edit_product_form.py")
            
            col6_2 = st.container()
            if col6_2.button('Delete', key=f"approve_{product[0]}"):
                delete_product(product[0])
                st.rerun()

if st.button("Add Product", key="add_product", type="primary"):
    st.switch_page("pages/add_product.py")

if st.session_state.selected == "Manage Customers":
    st.switch_page("pages/a_dashboard.py")
elif st.session_state.selected == "Manage Orders":
    st.switch_page("pages/manage_orders.py")