import streamlit as st

pg = st.navigation([
    st.Page("pages/login.py"),
    st.Page("pages/signup.py"),
    st.Page("pages/a_dashboard.py"),
    st.Page("pages/s_dashboard.py"),
    st.Page("pages/edit_form.py"),
    st.Page("pages/manage_products.py"),
    st.Page("pages/edit_product_form.py"),
    st.Page("pages/add_product.py"),
    st.Page("pages/manage_orders.py"),
    st.Page("pages/basket.py"),
    st.Page("pages/history.py"),
], position="hidden")

pg.run()