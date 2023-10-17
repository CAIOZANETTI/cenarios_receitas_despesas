import streamlit as st
import pandas as pd

import fx_dados as fx_dados

if 'input' not in st.session_state:
	st.session_state['input']={}

if 'analise' not in st.session_state:
	st.session_state['analise']={}

if 'inputs' not in st.session_state:
	st.session_state['inputs']=[]
	st.session_state['ativo_excluir']=False


with st.expander('parametros iniciais',expanded=False):
	cols =st.columns([1,1,1])
	st.session_state['analise']['periodo'] = cols[0].slider('periodo',12,60,value=12)
	st.session_state['analise']['loops'] = cols[1].slider('loops',10,100,value=50)
	st.session_state['analise']['quartil']=cols[2].slider('quartil',5,100,value=50)

	st.write(st.session_state['analise'])
	#st.dataframe(df_analise)

with st.expander('Curva Composta',expanded=True):

	cols =st.columns([1,1,1,1,1,1,1])
	st.session_state['input']['tipo'] = cols[0].radio('tipo',['despesa','receita'])
	
	fluxos = ['aleatorio','parcela-fixa','financiamento price','recorrente']
	st.session_state['input']['curva'] = cols[1].radio('distribuição',fluxos)
	
	fx_math = ['somar','multicar','divir','subtrair']
	st.session_state['input']['fx_math'] = cols[2].radio('Agregar',fx_math)

	if st.session_state['input']['curva'] =='aleatorio':
		cols[3].text('saida')
		st.session_state['input']['inteiro'] = cols[3].checkbox('inteiro')
		st.session_state['input']['menor'] = cols[4].number_input('menor')
		st.session_state['input']['maior'] = cols[5].number_input('maior')
		
		cols[6].text('incluir')
		cols[6].button('sim',type='primary',key='btn_incluir')

	st.write(st.session_state['input'])
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

