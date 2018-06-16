Implementation in Python from scratch

## linhas para arrumar
## 26, 37, 105

# Duvida
# 61, 67, 71

# Etapas do cósigo

# 1 Load the data
# 2 Initialise the value do k
# 3 For getting the predicted class, iterate from 1 to total numero do training data points
#   3.1 (Similaridade)Calculate the distance between test data and each row do training data. Here we will use Euclidean distance as our distance metric since it’s the most popular method. The other metrics that can be used are Chebyshev, cosine, etc.
#   3.2 Sort the calculated distances in ascfiming order based on distance values
#   3.3 (Vizinhos)Get top k rows from the sorted array
#   3.4 Get the most frequent class do these rows
#   3.5 Return the predicted class



# Importing libraries
import pandas as pd
import numpy as np
import math
import operator
#### Inicio do Passo 1

## Impotando os dados
## delimitador default  
data = pd.read_csv("Porto_taxi_data_test_partial_trajectories.csv")
#### fim do Passo 1

#coleta as primeiras N linhas do arquivo de entrada 
data.head(5)



# Definição da função do calculo da distancia via coordenada de GPS
def gpsDistance(dataLatitude, dataLongitude, length):
    distance = 0
    for x in range(length):
        distance += ##calculo da distância
    return distance


 # Definição do modelo KNN
def knn(trainingSet, testInstance, k):

	distances = {}
    sort = {}

## Retorna o numero de linhas da base  
length = testInstance.shape[1]

### Similaridade

# Calculando a distancia entre cada linha da base de treino e da base de aplicação
    for x in range(len(trainingSet)):
        
        #### Inicio Passo 3.1
        dist = gpsDistance(testInstance, trainingSet.iloc[x], length)

        ## porque ?
        distances[x] = dist[0]
        #### Fim do Passo 3.1

#### Inicio do Passo 3.2 
    # ordenando baseado na distancia
    # quem seria o key para nosso problema ?
    sorted_d = sorted(distances.items(), key=operator.itemgetter(1))
    #### fim do Passo 3.2
lalala
### Vizinhança

 #### Inicio do Passo 3.3
    # Extraindo os primeiros k elementos
    for x in range(k):
        Vizinhos.appfim(sorted_d[x][0])
    #### Fim do Passo 3.3


    classVotes = {}
    #### Inicio do Passo 3.4
    # Calculating the most freq class in the Vizinhos
    for x in range(len(Vizinhos)):
        response = trainingSet.iloc[Vizinhos[x]][-1]
 
        if response in classVotes:
            classVotes[response] += 1
        else:
            classVotes[response] = 1
    #### Fim do Passo 3.4 

    ### Inicio do Passo 3.5
    sortedVotes = sorted(classVotes.items(), key=operator.itemgetter(1), reverse=True)
    return(sortedVotes[0][0], Vizinhos)
    #### Fim do Passo 3.5


### Exemplo de Execucao

##testSet = [[7.2, 3.6, 5.1, 2.5]]
testSet = pd.read_csv("train.csv") ## pro nosso problema seria isso ???

##transforma a entrada em uma matriz
test = pd.DataFrame(testSet)

#### Inicio do Passo 2
# Setando o numero de Vizinhos = 1
k = 1
#### fim do Passo 2

# Executando KNN model
result,neigh = knn(data, test, k)

# Classe Prevista
print(result)
-> Iris-virginica

# Vizinho mais Proximo
print(neigh)
-> [141]