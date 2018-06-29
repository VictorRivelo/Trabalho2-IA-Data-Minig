#http://scikit-learn.org/stable/modules/generated/sklearn.neighbors.KNeighborsClassifier.html

#KNeighborsClassifier(n_neighbors=5, weights=’uniform’, algorithm=’auto’, leaf_size=30, p=2, metric=’minkowski’, #metric_params=None, n_jobs=1)

import pandas as pd
import numpy as np
import threading
import re
import discretiza_trajetorias as dt
from sklearn.neighbors import KNeighborsClassifier
from sklearn import tree

def main():
	dados = pd.read_csv('DADOS_TREINAMENTO_REDUZIDO.csv')
	matriz_discretizada = dt.discretiza_trajetorias(dados, 100, True)
	print('matriz discretizada na main')
	print(matriz_discretizada)

	matriz_atributos = matriz_discretizada.loc[:,'TRIP_ID':'classe_lat'].iloc[:,:-1]
	matriz_classes = matriz_discretizada.loc[:,'classe_lat':'classe_long']
	print(matriz_discretizada.loc[:,'TRIP_ID':'classe_lat'].iloc[:,:-1])
	print(matriz_classes)

	classificador = tree.DecisionTreeClassifier()
	classificador = classificador.fit(matriz_atributos, matriz_classes['classe_lat'])
	print('EXIBINDO ARVORE')
	print(classificador)
	return 0

main()