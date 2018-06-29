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


def haversine(lat1, lon1, lat2, lon2):

      R = 3959.87433 # this is in miles.  For Earth radius in kilometers use 6372.8 km

      dLat = math.radians(lat2 - lat1)
      dLon = math.radians(lon2 - lon1)
      lat1 = math.radians(lat1)
      lat2 = math.radians(lat2)

      a = math.sin(dLat/2)**2 + math.cos(lat1)*math.cos(lat2)*math.sin(dLon/2)**2
      c = 2*math.asin(math.sqrt(a))

      return R * c

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

    return geopy.distance.vincenty(coords_1, coords_2).km


def delimitadorless(Coordenada):
    
    return Coordenada.strip('(').strip(']').split(',')
  
def media(Matriz_distancias1):
    
    return  (float(delimitadorless(Matriz_distancias1)[0]) + float(delimitadorless(Matriz_distancias1)[1])) / 2
    

def distMedia(arquivoPreProcessado):

    Matriz_distancias = pd.DataFrame()
    data = pd.read_csv('dados_preprocessados.csv') 
    data2 = pd.read_csv('DADOS_TREINAMENTO_REDUZIDO.csv') 
    Matriz_distancias = (data['lat0'], data['long0'], data['classe_lat'], data['classe_long'], data2['TRIP_ID']) 
    
    mediaLat0 = media(Matriz_distancias[0][0]) 
    mediaLong0 = media(Matriz_distancias[1][0]) 
    mediaClassLat = media(Matriz_distancias[2][0]) 
    mediaClassLong = media(Matriz_distancias[3][0]) 

    #distance = distance1(mediaLat0, mediaLong0 ,mediaClassLat, mediaClassLong)
    #haversine = haversine(mediaLat0, mediaLong0 ,mediaClassLat, mediaClassLong)
  
    size =  len(Matriz_distancias[4])
    for i in range(0, size): 
        
        mediaLat0 = media(Matriz_distancias[0][i]) 
        mediaLong0 = media(Matriz_distancias[1][i]) 
        mediaClassLat = media(Matriz_distancias[2][i]) 
        mediaClassLong = media(Matriz_distancias[3][i])
        distance = distance1(mediaLat0, mediaLong0 ,mediaClassLat, mediaClassLong)
        Matriz_distancias['Media_Distancia'] = distance

  
    return 0

distMedia('dados_preprocessados.csv')




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
