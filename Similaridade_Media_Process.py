##Converter as coordenadas em um local em um ponto
def gpsdData(dataLatitude, dataLongitude):

    return 

##calcular a dist entre dois pontos
##latitude e longitude utilizadas em segundos

import math
public double distancia (int latitudeOrigem, int longitudeOrigem, int latitudeDestino, int longitudeDestino){

      double circTerra=40030; // Circunferência da Terra (em kilômetros)
      double latitudeO = (double) latitudeOrigem / 3600;
      double longitudeO = (double) longitudeOrigem / 3600;
      double latitudeD = (double) latitudeDestino / 3600;
      double longitudeD = (double) longitudeDestino / 3600;
      double a = longitudeO - longitudeD;
      double c = 90.0 - latitudeO;
      double b = 90.0 - latitudeD;       
      double aCosA =  (Math.acos(Math.cos(radians(b)) * Math.cos(radians(c)) + Math.sin(radians(b)) * Math.sin(radians(c)) * Math.cos(radians(a))) * 180 / Math.PI);

      return(aCosA * circTerra / 360);
} 

##Calcula a dist média para cada motorista 

def distMedia():

    return 
