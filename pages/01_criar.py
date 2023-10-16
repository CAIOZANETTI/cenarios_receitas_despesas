import streamlit as st

st.write('teste')

cols =st.columns([1,1,1])
fluxos = ['aleatorio','parcela fixa','financiamento price','recorrente']
cols[0].radio('tipo fluxo',fluxos,key='curva')

if st.session_state['curva'] =='aleatorio':
	cols[1].slider('min_maxte'5,10,key='min_max')


cols[2].write(st.session_state['min_maxte'])