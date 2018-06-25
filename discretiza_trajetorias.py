import pandas as pd
import numpy as np
import threading
import re

def discretiza_trajetorias(numero_de_quadrantes, precisa_separar_lat_long):
	matriz_lat_long_separadas = pd.DataFrame()
	if(precisa_separar_lat_long):
		data = pd.read_csv('DADOS_TREINAMENTO_REDUZIDO.csv')
		matriz_com_coordenadas_em_colunas = separa_polyline_em_colunas(data)

		matriz_apenas_com_coordenadas = matriz_com_coordenadas_em_colunas.loc[:,'coord0':]
		#print(matriz_coordenadas)
		#print(matriz_coordenadas.loc[1:500])

		'''
		threads = []
		total_dados = len(matriz_coordenadas.index)
		qtd_threads = 4
		intervalos = np.linspace(start=0, stop=total_dados, dtype=int, num=qtd_threads)
		print(intervalos)
	
	
		for i in range(qtd_threads-1):
		#inicio_intervalo = i*500
		#fim_intervalo = (i+1)*500-1
		nova_thread = threading.Thread(target=separa_latitude_e_longitude, args=(matriz_coordenadas.loc[intervalos[i]:intervalos[i+1]-1],i,intervalos[i], intervalos[i+1]-1))
		threads.append(nova_thread)
		nova_thread.start()
		print(i)'''
	
		print('vai separar lat e long')
		matriz_lat_long_separadas = separa_latitude_e_longitude(matriz_apenas_com_coordenadas)
		matriz_lat_long_separadas.to_csv('dados_sem_colchete.csv')
	else:
		matriz_lat_long_separadas = pd.read_csv('dados_sem_colchete.csv')
		print('dados lidos do arquivo')
		print(matriz_lat_long_separadas)

	print('lat0')
	print(matriz_lat_long_separadas['lat0'])
	print('long0')
	print(matriz_lat_long_separadas['long0'])
	print('convertendo tudo em numerico')
	#print(matriz_lat_long_separadas)
	#print(latitudes)
	#print(longitudes)

	intervalos_latitude = calcula_intervalos_de_discretizacao(matriz_lat_long_separadas['lat0'], numero_de_quadrantes)
	print('intervalos da latitude')
	print(intervalos_latitude)

	intervalos_longitude = calcula_intervalos_de_discretizacao(matriz_lat_long_separadas['long0'], numero_de_quadrantes)
	print('intervalos da longitude')
	print(intervalos_longitude)
	
	print('matriz sendo discretizada')
	print(matriz_lat_long_separadas)
	i = 0
	for column in matriz_lat_long_separadas:
		if(i % 2 == 0):
			matriz_lat_long_separadas[column] = pd.cut(x=matriz_lat_long_separadas[column], bins=intervalos_latitude)
			print('coluna discretizada com latitude')
			print(matriz_lat_long_separadas[column])
		else:
			matriz_lat_long_separadas[column] = pd.cut(x=matriz_lat_long_separadas[column], bins=intervalos_longitude)
			print('coluna discretizada com longitude')
			print(matriz_lat_long_separadas[column])
		i += 1

	print('matriz discretizada')
	print(matriz_lat_long_separadas)
	
	move_classe_para_ultima_coluna(matriz_lat_long_separadas)
	
	matriz_lat_long_separadas.to_csv('dados_preprocessados.csv')

	return 0

def move_classe_para_ultima_coluna(dados):
	matriz_nula = pd.isnull(dados)
	print(matriz_nula)

	i = 0
	matriz_com_classe = pd.DataFrame()
	for index, linha in dados.iterrows():
		print('linha',i)
		ultimo_indice_valido = linha.last_valid_index()
		print('ultimo indice valido', ultimo_indice_valido,'valor',linha[ultimo_indice_valido])
		numero_ultimo_indice_valido = int(re.findall(r'\d+', ultimo_indice_valido)[0])
		print('numero ultimo_indice_valido', numero_ultimo_indice_valido)
		linha['classe_lat'] = linha['lat'+str(numero_ultimo_indice_valido)]
		linha['classe_long'] = linha['long'+str(numero_ultimo_indice_valido)]
		print('classe lat linha', linha['classe_lat'])
		print('classe long linha', linha['classe_long'])
		#print(linha)
		i += 1
		matriz_com_classe = matriz_com_classe.append(linha)


	print('final: matriz com classe')
	print(matriz_com_classe)
	return matriz_com_classe

#def separa_latitude_e_longitude(dados, num_thread, inicio_intervalo, fim_intervalo):
def separa_latitude_e_longitude(dados):
	#print('thread que chamou', num_thread, 'inicio intervalo',inicio_intervalo,'fim intervalo',fim_intervalo,'qtd de dados',len(dados.index))
	#print(dados)
	#	print('dado que chegou na funcao de separacao')
	#print(colunas.columns)
	#	print('matriz is null')
	
	matriz_lat_long_separadas = pd.DataFrame()
	j = 0
	for index, linha in dados.iterrows():
		i = 0
		qtd_colunas_validas = len(linha.tolist())-linha.isnull().sum()
		nova_linha = pd.Series()
		labels = []
		while (i < qtd_colunas_validas):
			coluna = linha[i].strip('[').strip(']')
			labels = ['lat'+str(i),'long'+str(i)]
			try:
				nova_linha = nova_linha.append(pd.Series(coluna.split(','), index=labels))
				#nova_linha[labels[0]] = nova_linha[labels[0]]
				#nova_linha[labels[1]] = nova_linha[labels[1]]
			except BaseException:
				print('EXCEPTION!!!!')
			i += 1

		#nova_linha = nova_linha.T
		print('fazendo linha', j)
		#print('linha resultante')
		#print(nova_linha)
		matriz_lat_long_separadas[j] = pd.to_numeric(nova_linha)

		#print('thread',num_thread,'colocou na matriz de lat e long j=', j)
		j += 1
	
	#rint('MATRIZ RESULTANTE DA THREAD ', num_thread)
	#matriz_lat_long_separadas.index += inicio_intervalo
	matriz_lat_long_separadas = matriz_lat_long_separadas.transpose()
	#matriz_lat_long_separadas = matriz_lat_long_separadas.shift(periods=inicio_intervalo, axis=0)
	print(matriz_lat_long_separadas)
	
			#print(matriz_lat_long_separadas)
	
		#print(matriz_lat_long_separadas)
		#break
	'''for coluna in colunas.columns:
			if(pd.isna(linha[coluna])):
				break
			else:
				#print('index',index)
				#print(index,'[',coluna,']=')
				#print(linha[coluna])
				lat_label = 'lat'+str(i)
				long_label = 'long'+str(i)

				coords_separadas = pd.DataFrame(colunas[coluna].str.split(',', expand=True))
				coords_separadas.columns = [lat_label, long_label]

				coords_separadas[lat_label] = coords_separadas[lat_label].str.strip('[')
				coords_separadas[lat_label] = pd.to_numeric(coords_separadas[lat_label])

				coords_separadas[long_label] = coords_separadas[long_label].str.strip(']')
				coords_separadas[long_label] = pd.to_numeric(coords_separadas[long_label])


				matriz_lat_long_separadas = matriz_lat_long_separadas.append(coords_separadas, sort=False)
				i += 1 '''

	return matriz_lat_long_separadas

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

discretiza_trajetorias(100, True)
