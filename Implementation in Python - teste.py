Implementation in Python from scratch

## linhas para arrumar
## 26, 37,  

# Duvida
# 61, 


# Etapas do cósigo

# 1 Load the data
# 2 Initialise the value of k
# 3 For getting the predicted class, iterate from 1 to total number of training data points
#   3.1 (Similaridade)Calculate the distance between test data and each row of training data. Here we will use Euclidean distance as our distance metric since it’s the most popular method. The other metrics that can be used are Chebyshev, cosine, etc.
#   3.2 Sort the calculated distances in ascending order based on distance values
#   3.3 (Vizinhos)Get top k rows from the sorted array
#   3.4 Get the most frequent class of these rows
#   3.5 Return the predicted class



# Importing libraries
import pandas as pd
import numpy as np
import math
import operator
#### Start of STEP 1
# Importing data 
data = pd.read_csv("train.csv")
#### End of STEP 1

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

##retorna o numero de linhas da base  
length = testInstance.shape[1]

# Calculando a distancia entre cada linha da base de treino e da base de aplicação
    for x in range(len(trainingSet)):
        
        #### Inicio passo 3.1
        dist = gpsDistance(testInstance, trainingSet.iloc[x], length)

        ## porque ?
        distances[x] = dist[0]
        #### Fim do passo 3.1

#### Inicio do Passo 3.2 
    # Sorting them on the basis of distance
    sorted_d = sorted(distances.items(), key=operator.itemgetter(1))
    #### End of STEP 3.2