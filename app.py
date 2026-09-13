import streamlit as st
st.title("BCG Project Manager Tool")
st.write("Deployed from London.")

project = st.text_input("Project name")
manager = st.text_input("Project manager")

if project:
    st.success(f"Project loaded: {project} - Manager: {manager}")