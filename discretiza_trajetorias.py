import pandas as pd

def discretiza_trajetorias(grid_size):

	data = pd.read_csv('DADOS_TREINAMENTO.csv')
	
	data['POLYLINE'] = data['POLYLINE'].str[1:]
	data['POLYLINE'] = data['POLYLINE'].str.replace('], ','];')
	d2 = data['POLYLINE'].str.split(';',expand=True)
	data = data.drop('POLYLINE', axis=1)
	data = data.join(d2)

	print(data)
	data.to_csv('dados_preprocessados.csv')

	return 0



discretiza_trajetorias(0)
