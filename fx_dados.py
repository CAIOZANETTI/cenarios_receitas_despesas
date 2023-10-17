from dataclasses import dataclass, asdict
import pandas as pd

@dataclass
class Fatores:
	periodo:int=12
	quartil:int=50
	loops:int=100

@dataclass
class Curvas(Fatores):
	tipo:str='despesa'
	curva:str='aleatoria'
	fx_math:str='somar'#dividir, multiplica, subtrair
	inteiro:bool=False
	menor:float=0
	maior:float=0
	
	def __post_init__(self):
		dic = asdict(self)
		self.colunas= [k for k,v in dic.items()]
		self.lst = [v for k,v in dic.items()]
		df = pd.DataFrame([self.lst],columns=self.colunas)
		df['media'] =(df['menor']+df['maior'])/2
		df['total_med'] =df['media']*df['prazo'] 

		self.df = df