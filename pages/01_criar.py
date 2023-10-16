import streamlit as st

st.write('teste')

cols =st.columns([1,1,1])
fluxos = ['aleatorio','parcela-fixa','financiamento price','recorrente']
cols[0].radio('tipo fluxo',fluxos,key='curva')

st.write(st.session_state['curva'])

if st.session_state['curva'] =='aleatorio':
	st.write('aleatorio')

	#cols[1].number_input('min')#,key='min')
	#cols[1].number_input('max',key='max')
	#cols[2].write(st.session_state['min'])
	#cols[2].write(st.session_state['max'])


if st.session_state['curva'] =='parcela-fixa':
	st.write('parcela-fixa')

