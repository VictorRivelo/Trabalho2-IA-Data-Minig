import pandas as pd
import numpy as np
import threading
import re

def discretiza_trajetorias(dados, numero_de_quadrantes, precisa_separar_lat_long):
	print('matriz original')
	print(dados)

	matriz_com_outros_dados = dados.loc[:,:'MISSING_DATA']

	matriz_discretizada = pd.DataFrame()
	if(precisa_separar_lat_long):
		matriz_discretizada = separa_polyline_em_latitudes_e_longitudes(dados)
		print('matriz com polyline quebrado')
		print(matriz_discretizada)

		print('matriz com outros dados')
		print(matriz_com_outros_dados)
	
		print('vai separar lat e long')
		matriz_discretizada.to_csv('dados_sem_colchete.csv')
	else:
		matriz_discretizada = dados.loc[:,'lat0':]

	intervalos_latitude = calcula_intervalos_de_discretizacao(matriz_discretizada['lat0'], numero_de_quadrantes)
	#print('intervalos da latitude')
	#print(intervalos_latitude)

	intervalos_longitude = calcula_intervalos_de_discretizacao(matriz_discretizada['long0'], numero_de_quadrantes)
	#print('intervalos da longitude')
	#print(intervalos_longitude)
	
	#print('matriz sendo discretizada')
	#print(matriz_discretizada)
	print('matriz antes de discretizar')
	print(matriz_discretizada)

	print('linha 117 antes de discretizar')
	print(matriz_discretizada.loc[117,:])

	
	i = 0
	print('discretizando')
	for column in matriz_discretizada.loc[:,'lat0'::2].columns:
		matriz_discretizada[column] = pd.cut(x=matriz_discretizada[column], bins=intervalos_latitude, include_lowest=True)
		#print('discretizacao da coluna latitude',column)
		#print(matriz_discretizada[column])
	
	for column in matriz_discretizada.loc[:,'long0'::2].columns:
		matriz_discretizada[column] = pd.cut(x=matriz_discretizada[column], bins=intervalos_longitude, include_lowest=True)
		#print('discretizacao da coluna longitude',column)
		#print(matriz_discretizada[column])		
	
	matriz_discretizada = move_classe_para_ultima_coluna(matriz_discretizada)

	print('resultado final')
	print(matriz_discretizada)

	matriz_discretizada.to_csv('dados_preprocessados.csv')

	return 0

def move_classe_para_ultima_coluna(dados):
	i = 0
	matriz_com_classe = pd.DataFrame()
	
	dados['classe_lat'] = np.nan
	dados['classe_long'] = np.nan
	print(dados)

	print('colocando classe na matriz')
	for index, linha in dados.iterrows():
		#print('detalhes da linha',linha.name)
		#print(linha)	

		#print('linha',i)
		ultimo_indice_valido = linha.last_valid_index()
		#print('ultimo indice valido', ultimo_indice_valido,'valor',nova_linha[ultimo_indice_valido])
		numero_ultimo_indice_valido = int(re.findall(r'\d+', ultimo_indice_valido)[0])
		#print('numero ultimo_indice_valido', numero_ultimo_indice_valido)
		label_latitude_ultimo_indice_valido = 'lat'+str(numero_ultimo_indice_valido)
		label_longitude_ultimo_indice_valido = 'long'+str(numero_ultimo_indice_valido)
		#print('valor do ultimo ponto da trajetoria')
		#print(linha[label_latitude_ultimo_indice_valido])
		print('linha',linha.name)
		print('numero do ultimo indice valido', numero_ultimo_indice_valido)
		print('valor')
		print(dados.loc[linha.name, label_latitude_ultimo_indice_valido])
		print(dados.loc[linha.name, label_longitude_ultimo_indice_valido])
		#print(linha[label_longitude_ultimo_indice_valido])

		#print('linha da matriz antes de receber a classe')
		#print(dados.loc[linha.name,:])
		dados.loc[linha.name,'classe_lat'] = linha[label_latitude_ultimo_indice_valido]
		dados.loc[linha.name,'classe_long'] = linha[label_longitude_ultimo_indice_valido]
		dados.loc[linha.name,label_latitude_ultimo_indice_valido] = np.nan
		dados.loc[linha.name,label_longitude_ultimo_indice_valido] = np.nan
	
		#print('linha da matriz que recebeu a classe')
		#print(dados.loc[linha.name,:])

		#break
		#print('linha depois de colocar a classe')
		#print(linha)
		
		#print('linha correspondente da matriz')
		#print(dados.loc[linha.name,:])
		#print(dados.loc[linha,:])

		#print('classe lat linha', nova_linha['classe_lat'])
		#print('classe long linha', nova_linha['classe_long'])
		#print(nova_linha.index)
		i += 1
		#print('nova linha')
		#print(nova_linha)
		#matriz_com_classe = matriz_com_classe.append(linha)[linha.index]
		#print('matriz com classe')
		#print(matriz_com_classe)

	
	#print('matriz com classe')
	#print(matriz_com_classe)
	print('coluna classe da matriz final')
	print(dados['classe_lat'])
	print(dados['classe_long'])
	#matriz_pontos = matriz_com_classe.loc[:,'lat5':'classe_lat'].iloc[:-1]
	#print('matriz fatiada')
	#print(matriz_pontos)
	return dados

#def separa_latitude_e_longitude(dados, num_thread, inicio_intervalo, fim_intervalo):
def separa_coordenadas_em_latitude_e_longitude(dados):
	#print('thread que chamou', num_thread, 'inicio intervalo',inicio_intervalo,'fim intervalo',fim_intervalo,'qtd de dados',len(dados.index))
	#print(dados)
	#	print('dado que chegou na funcao de separacao')
	#print(colunas.columns)
	#	print('matriz is null')


	colunas = dados.loc[:,'coord0':]
	print('colunas selecionadas pra quebrar em latitude e longitude')
	print(colunas)
	
	
	i = 0
	#for index, linha in dados.iterrows():
	#	i = 0
	#	qtd_colunas_validas = len(linha.tolist())-linha.isnull().sum()
	#	nova_linha = pd.Series()
	#	labels = []
	for coluna in colunas.columns:

		#print('quebrando a coluna',coluna)
		#print('iterando sobre a coluna', coluna)
		#print(dados[coluna])
		#print('tirando []')
		dados[coluna] = dados[coluna].str.strip('[]')
		#print(dados[coluna])
		labels = ['lat'+str(i),'long'+str(i)]
		#print(labels)
		#print('vai quebrar a coluna da matriz')
		try:
			temp_df = dados[coluna].str.split(',',expand=True).astype(float)
			temp_df.columns = labels
			dados['lat'+str(i)] = temp_df['lat'+str(i)]
			dados['long'+str(i)] = temp_df['long'+str(i)]
			dados = dados.drop(['coord'+str(i)], axis=1)
		except BaseException:
			print('Pulando linha...')
		#print('coluna quebrada')
		#print(temp_df)
		#print('novo estado da matriz')
		#print(dados['lat0'])
		#print(dados['long0'])
		#print('tirando a coordenada antiga')
		#print(dados)
		i += 1

	#print('matriz final')
	#print(dados)
	return dados

def calcula_intervalos_de_discretizacao(coluna, numero_de_quadrantes):
	max_coluna, min_coluna, range_coluna = calcula_range_da_coluna(coluna)
	intervalos = np.linspace(start=min_coluna, stop=max_coluna, num=numero_de_quadrantes)
	print('range', range_coluna)
	return intervalos

def calcula_range_da_coluna(column):
	column = pd.to_numeric(column)
	statistics = column.describe()
	print(statistics)
	column_max = statistics['max']
	column_min = statistics['min']
	column_range = np.absolute(column_max-column_min)
	print(statistics)
	print('max', column_max)
	print('min', column_min)
	print('range', column_range)
	return column_max, column_min, column_range

def separa_polyline_em_latitudes_e_longitudes(data):
	print('matriz que vai ser ter a polyline separada em colunas')
	print(data)
	matriz_com_coordenadas_em_colunas = separa_polyline_em_colunas_de_coordenadas(data)
	print('separou polyline em coordenadas')
	print(matriz_com_coordenadas_em_colunas)
	print('vai separar as coordenadas em latitude e longitude')
	matriz_com_coordenadas_em_colunas = separa_coordenadas_em_latitude_e_longitude(matriz_com_coordenadas_em_colunas)
	return matriz_com_coordenadas_em_colunas

def separa_polyline_em_colunas_de_coordenadas(data):
	data = formata_polyline_para_separacao(data)

	polyline_separado = data['POLYLINE'].str.split(';',expand=True)

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
	print('num colunas', column_num)
	columns = []	
	for x in range(column_num):
		columns.append('coord'+str(x))

	return columns

dados = pd.read_csv('DADOS_TREINAMENTO_REDUZIDO.csv')
discretiza_trajetorias(dados, 100, True)
