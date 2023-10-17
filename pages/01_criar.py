import streamlit as st
import pandas as pd

import fx_dados as fx_dados

if 'input' not in st.session_state:
	st.session_state['input']={}

if 'fatores' not in st.session_state:
	st.session_state['fatores']={}

if 'inputs' not in st.session_state:
	st.session_state['inputs']=[]
	st.session_state['ativo_excluir']=False


with st.expander('parametros iniciais',expanded=False):
	cols =st.columns([1,1,1])
	st.session_state['fatores']['periodo'] = cols[0].slider('periodo',12,60,value=12)
	st.session_state['fatores']['loops'] = cols[1].slider('loops',10,100,value=50)
	st.session_state['fatores']['quartil']=cols[2].slider('quartil',5,100,value=50)

	st.write(st.session_state['fatores'])
	curva = fx_dados.Fatores(**st.session_state['fatores'])

with st.expander('Curva Probabilista Calculada',expanded=True):

	cols =st.columns([1,1,1,1,1,1,1,1])
	
	cols[0].write('quantidade')
	st.session_state['input']['calc_qtd']['tipo'] = cols[1].checkbox('inteiro')
	st.session_state['input']['calc_qtd']['nome'] = cols[2].text_input('nome')
	st.session_state['input']['calc_qtd']['menor'] = cols[3].number_input('menor')
	st.session_state['input']['calc_qtd']['maior'] = cols[4].number_input('maior')
	
	cols =st.columns([1,1])	
	cols[0].text('Probabilidade')
	cols[0].button('Calcular',type='primary',key='btn_calcular')
	
	st.write(session_state)

"""
	curva = fx_dados.Curvas(**st.session_state['input'])
	st.dataframe(curva.df)


	if st.session_state['input']['curva'] =='parcela-fixa':
		st.write('parcela-fixa')

	if st.session_state['btn_incluir']==True:
		st.session_state['inputs'].append(st.session_state['input'])


with st.expander('Resumos',expanded=True):
	st.write(st.session_state['inputs'])

	df = pd.DataFrame()
	st.dataframe(df)

	st.markdown("""---""")
	cols =st.columns([1,1,1])
	if len(st.session_state['inputs'])>1:
		st.session_state['ativo_excluir']=True

	cols[1].button('deletar ultimo',key='btn_excluir',disabled=st.session_state['ativo_excluir'])
	cols[2].button('limpar tudo',key='btn_limpar')

	if st.session_state['btn_incluir']==True:
			st.session_state['inputs']=[]

	if st.session_state['btn_excluir']==True:
			st.session_state['inputs']=[]


with st.expander('session_state',expanded=True):
	st.write(st.session_state['input'])

"""