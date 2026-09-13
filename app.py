import streamlit as st
st.title("BCG Project Manager Tool")
st.write("If you can read this, your first app is running.")

project = st.text_input("Project name")

if project:
    st.success(f"Project loaded: {project}")