import streamlit as st

st.title("Class Activity 23")

col1, col2 = st.columns(2)

with col1:
    col1.header("Column 1")
    col1.write("Hello")

with col2:
    col2.header("Column 2")
    col2.write("World")

ex = st.expander("expand for more information")
ex.write("Here you could put in some explanatory stuff")
