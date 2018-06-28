# -*- coding: utf-8 -*-
"""
Created on Wed Jun 27 17:49:42 2018

@author: CPU
"""

##calcular a dist entre dois pontos
##latitude e longitude utilizadas em segundos

## teste1, erro de 0,5% aproximadamente
import math
import pandas as pd
import numpy as np
#import geopy.distance
#from geopy.distance import geodesic

def delimitadorless(Coordenada):
    
    return Coordenada.strip('(').strip(']').split(',')
  

def distMedia(arquivoPreProcessado):

    Matriz_distancias = pd.DataFrame()
    data = pd.read_csv('dados_preprocessados.csv') 
   
    Matriz_distancias = (data['lat0'], data['long0'], data['classe_lat'], data['classe_long'])    

    mediaLat= ((delimitadorless(Matriz_distancias[0][0])[0]).to_numeric + (delimitadorless(Matriz_distancias[0][0])[1])).to_numeric / 2
    mediaLong= ((delimitadorless(Matriz_distancias[1][0])[0]).to_numeric + (delimitadorless(Matriz_distancias[1][0])[1])).to_numeric / 2
    print(mediaLat)
    print(mediaLong)
    
    distance1(mediaLat, mediaLong)    
    
  #  for i in range  
  #     mediaLat=(((delimitadorless(Matriz_distancias[0][0])[1]) + (delimitadorless(Matriz_distancias[0][0])[2])) / 2)
  #     mediaLong=(((delimitadorless(Matriz_distancias[1][1])[1]) + (delimitadorless(Matriz_distancias[1][1])[2])) / 2)
  #  print(Matriz_distancias[0].min)
    
    

    return 0

distMedia('dados_preprocessados.csv')

def distance1(originlatitude, originlongitude, destLatitude, destLongitude):
    
    lat1 = originlatitude
    lon1 = originlongitude
    lat2 = destLatitude
    lon2 = destLongitude
    radius = 6371 # km

    dlat = math.radians(lat2-lat1)
    dlon = math.radians(lon2-lon1)
    a = math.sin(dlat/2) * math.sin(dlat/2) + math.cos(math.radians(lat1)) \
        * math.cos(math.radians(lat2)) * math.sin(dlon/2) * math.sin(dlon/2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1-a))
    d = (radius * c)

    return d

##teste2
def distance2(originlatitude, originlongitude, destLatitude, destLongitude):

    coords_1 = (originlatitude, originlongitude)
    coords_2 = (destLatitude, destLongitude)

    return geopy.distance.vincenty(coords_1, coords_2).km

##teste 3 


def distance3(originlatitude, originlongitude, destLatitude, destLongitude):
    coords_1 = (originlatitude, originlongitude)
    coords_2 = (destLatitude, destLongitude)

    return (geodesic(coords_1, coords_2).miles * 1,60934)





##Calcula a dist média para cada motorista 



#http://minerandodados.com.br/index.php/2017/09/26/python-para-analise-de-dados/
'''def categoriza(s):
if s >= 80:
       return 'Big'
    elif s >= 60:
       return 'Medium'
    elif s >= 40:
       return 'Small'
       
ataset['cat_size'] = dataset['size'].apply(categoriza)
'''
