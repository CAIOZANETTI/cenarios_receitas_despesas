import streamlit as st

st.write('teste')

cols =st.columns([1,1,1])
fluxos = ['aleatorio','parcela-fixa','financiamento price','recorrente']
cols[0].radio('tipo fluxo',fluxos,key='curva')

st.write(st.session_state['curva'])

if st.session_state['curva'] =='aleatorio':
	cols[1].write('aleatorio')

	cols[1].number_input('min')
	cols[2].number_input('max')
	
	
if st.session_state['curva'] =='parcela-fixa':
	st.write('parcela-fixa')

