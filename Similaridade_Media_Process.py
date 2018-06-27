##calcular a dist entre dois pontos
##latitude e longitude utilizadas em segundos

## teste1, erro de 0,5% aproximadamente
import math

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
    d = radius * c

    return d
} 

##teste2
import geopy.distance

def distance2(originlatitude, originlongitude, destLatitude, destLongitude):

coords_1 = (originlatitude, originlongitude)
coords_2 = (destLatitude, destLongitude)

return geopy.distance.vincenty(coords_1, coords_2).km

##teste 3 
from geopy.distance import geodesic

def distance3(originlatitude, originlongitude, destLatitude, destLongitude):
coords_1 = (originlatitude, originlongitude)
coords_2 = (destLatitude, destLongitude)

return (geodesic(coords_1, coords_2).miles * 1,60934)



##Calcula a dist média para cada motorista 
import pandas as pd
import numpy as np

def distMedia(arquivoPreProcessado):

Matriz_distancias = pd.DataFrame()
data = pd.read_csv('dados_preprocessados.csv') 

 (data.columns - 1) 





    return 0

