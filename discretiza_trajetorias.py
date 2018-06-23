import pandas as pd

def discretiza_trajetorias(grid_size):

	data = pd.read_csv('DADOS_TREINAMENTO.csv')
	#split_data = pd.DataFrame().row.str.split()
	data['POLYLINE'] = data['POLYLINE'].str[1:]
	data['POLYLINE'] = data['POLYLINE'].str.replace('], ','];')
	
	data_split = data['POLYLINE'].apply(lambda x: pd.DataFrame(x.split(';')))

	print(data_split)
	data_split.to_csv('dados_preprocessados.csv')

	return 0



discretiza_trajetorias(0)
