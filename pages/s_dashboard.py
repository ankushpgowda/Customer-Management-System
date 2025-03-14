import streamlit as st
from streamlit_option_menu import option_menu
from backend import get_products, add_to_basket
st.set_page_config(layout="wide")

with st.sidebar:
    st.title(f"Welcome :red[{st.session_state.firstname}] !")
    st.markdown(" ")
    st.session_state.selected = option_menu(
        menu_title=None,
        options=["Store", "Basket", "Order's History"],
        icons=["shop", "basket", "hourglass"],
        default_index=0
    )
    st.page_link("pages/login.py", label="Logout")

st.title("Store")
with st.container(border=True):
    col1, col2, col3, col4, col5, col6 = st.columns(6)
    col1.write(f"Product:")
    col2.write(f"Product Name:")
    col3.write(f"Description:")
    col4.write(f"Unit Price:")
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
        units = col5.number_input(f"Add Units", key=f"unit_{product[0]}", format="%d", value=0, step=1,)
        with col6.container():
            
            col6_1 = st.container()
            if col6_1.button('Add', key=f"edit_{product[0]}"):
                add_to_basket(product[0], units)
                st.success(f"{units} units of {product[1]} is added in your basket")

if st.session_state.selected == "Basket":
    st.switch_page("pages/basket.py")
elif st.session_state.selected == "Order's History":
    st.switch_page("pages/history.py")