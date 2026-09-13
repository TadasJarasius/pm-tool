import streamlit as st
st.title("BCG Project Manager Tool")
st.write("Deployed from London.")

project = st.text_input("Project name")

if project:
    st.success(f"Project loaded: {project}")