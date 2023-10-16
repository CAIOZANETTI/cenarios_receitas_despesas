import streamlit as st


with open('README.md', 'r', encoding='utf-8') as file:
	contents = file.read()
	st.markdown(contents)
