import streamlit as st

st.write('teste')


with open('README.md', 'r', encoding='utf-8') as file:
	contents = file.read()
	st.markdown(contents)
