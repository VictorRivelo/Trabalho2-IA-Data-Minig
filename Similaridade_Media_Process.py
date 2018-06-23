##Converter as coordenadas em um local em um ponto
def gpsdData(dataLatitude, dataLongitude):

    return 

##calcular a dist entre dois pontos
##latitude e longitude utilizadas em segundos

## teste1, erro de 0,5% aproximadamente
import math

def distance(originlatitude, originlongitude, destLatitude, destLongitude):
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

def distance(originlatitude, originlongitude, destLatitude, destLongitude):

coords_1 = (originlatitude, originlongitude)
coords_2 = (destLatitude, destLongitude)

print geopy.distance.vincenty(coords_1, coords_2).km

##Calcula a dist média para cada motorista 

def distMedia():

    return 
