import pandas as pd
import numpy as np

def discretiza_trajetorias(numero_de_quadrantes):
	data = pd.read_csv('DADOS_TREINAMENTO.csv')
	data = separa_polyline_em_colunas(data)

	
	latitudes, longitudes = separa_latitude_e_longitude(data['coord0'])
	print(latitudes)
	print(longitudes)

	intervalos_latitude = calcula_intervalos_de_discretizacao(latitudes, numero_de_quadrantes)
	print('intervalos da latitude')
	print(intervalos_latitude)

	intervalos_longitude = calcula_intervalos_de_discretizacao(longitudes, numero_de_quadrantes)
	print('intervalos da longitude')
	print(intervalos_longitude)


	latitudes = pd.cut(x=latitudes, bins=intervalos_latitude)
	longitudes = pd.cut(x=longitudes, bins=intervalos_longitude)
	print('coordenadas discretizadas')
	print(latitudes)
	print(longitudes)

	data.to_csv('dados_preprocessados.csv')

	return 0

def separa_latitude_e_longitude(coluna):
	coords_separadas = pd.DataFrame(coluna.str.split(',', expand=True))
	coords_separadas.columns = ['lat0','long0']

	coords_separadas['lat0'] = coords_separadas['lat0'].str.strip('[')
	coords_separadas['lat0'] = pd.to_numeric(coords_separadas['lat0'])

	coords_separadas['long0'] = coords_separadas['long0'].str.strip(']')
	coords_separadas['long0'] = pd.to_numeric(coords_separadas['long0'])

	return coords_separadas['lat0'], coords_separadas['long0']


def calcula_intervalos_de_discretizacao(coluna, numero_de_quadrantes):
	max_coluna, min_coluna, range_coluna = calcula_range_da_coluna(coluna)
	intervalos = np.linspace(start=min_coluna, stop=max_coluna, num=numero_de_quadrantes)
	print('range', range_coluna)
	return intervalos

def calcula_range_da_coluna(column):
	statistics = column.describe()
	column_max = statistics['max']
	column_min = statistics['min']
	column_range = np.absolute(column_max-column_min)
	print(statistics)
	print('max', column_max)
	print('min', column_min)
	print('range', column_range)
	return column_max, column_min, column_range

def separa_polyline_em_colunas(data):
	data = formata_polyline_para_separacao(data)

	polyline_separado = data['POLYLINE'].str.split(';',expand=True)
	print('numero de colunas em d2 ', len(polyline_separado.columns))

	columns = monta_labels_das_colunas_da_trajetoria(len(polyline_separado.columns))
	polyline_separado.columns = columns

	data = data.drop('POLYLINE', axis=1)
	data = data.join(polyline_separado)
	return data

def formata_polyline_para_separacao(data):
	data['POLYLINE'] = data['POLYLINE'].str[1:]
	data['POLYLINE'] = data['POLYLINE'].str[:-1]
	data['POLYLINE'] = data['POLYLINE'].str.replace('], ','];')	
	return data

def monta_labels_das_colunas_da_trajetoria(column_num):
	columns = []	
	for x in range(column_num-1):
		columns.append('coord'+str(x))

	columns.append('classe')
	return columns

discretiza_trajetorias(100)
