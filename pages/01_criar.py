import streamlit as st

with st.expander('parametros iniciais',expanded=False):
	cols =st.columns([1,1,1])
	cols[0].slider('periodo',12,60,value=12)
	cols[1].slider('loops',10,100,value=50)
	cols[2].slider('quartil',5,100,value=50)

with st.expander('Curva Composta',expanded=False):


	cols =st.columns([1,1,1,1])
	cols[0].radio('tipo fluxo',['receita','despesa'],key='tipo')
	fluxos = ['aleatorio','parcela-fixa','financiamento price','recorrente']
	cols[1].radio('tipo fluxo',fluxos,key='curva')
	agg = ['+','-','*','/']
	
	st.write(st.session_state['curva'])

	if st.session_state['curva'] =='aleatorio':
		cols[2].number_input('min')
		cols[3].number_input('max')
		
		
	if st.session_state['curva'] =='parcela-fixa':
		st.write('parcela-fixa')

