import streamlit as st
import pandas as pd

if 'dic' not in st.session_state:
	st.session_state['dic']={}

with st.expander('parametros iniciais',expanded=False):
	cols =st.columns([1,1,1])
	cols[0].slider('periodo',12,60,value=12)
	cols[1].slider('loops',10,100,value=50)
	cols[2].slider('quartil',5,100,value=50)

with st.expander('Curva Composta',expanded=True):

	cols =st.columns([1,1,1,1,1,1])
	cols[0].radio('tipo',['receita','despesa'],key='tipo')
	
	fluxos = ['aleatorio','parcela-fixa','financiamento price','recorrente']
	cols[1].radio('distribuição',fluxos,key='curva')
	
	fx_math = ['soma','mult','divir','subtrair']
	cols[2].radio('Agregar',fx_math,key='fx_math')

	if st.session_state['curva'] =='aleatorio':
		cols[3].checkbox('inteiro',key='inteiro')
		cols[4].number_input('min',key='min')
		cols[5].number_input('max',key='max')
		
		
	if st.session_state['curva'] =='parcela-fixa':
		st.write('parcela-fixa')

	cols =st.columns([1,1,1])
	cols[0].button('incluir')
	cols[1].button('deletar')
	cols[2].button('limpar')

with st.expander('Resumos',expanded=True):
	df = pd.DataFrame()
	st.dataframe(df)

with st.expander('session_state',expanded=True):
	st.write(st.session_state)