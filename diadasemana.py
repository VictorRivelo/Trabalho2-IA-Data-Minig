import datetime
import pandas as pd

colnames = ['TRIP_ID', 'CALL_TYPE', 'ORIGIN_CALL', 'ORIGIN_STAND', 'TAXI_ID', 'TIMESTAMP', 'DAY_TYPE', 'MISSING_DATA', 'POLYLINE']
file = pd.read_csv('DADOS_TREINAMENTO_REDUZIDO.csv', names=colnames)

timestamp = file.TIMESTAMP.tolist()

size = len(timestamp) - 1

# listas dos valores de ANO, MÊS e DIA dos TIMESTAMPS
d_ano_l = []
d_mes_l = []
d_dia_l = []
d_weekday_l = []

for x in range(0, size):
    # transforma o timestamp em uma DATA (ANO-MÊS-DIA) -->> DATA = objeto
    d = datetime.date.fromtimestamp(int(timestamp[x+1])) # o primeiro valor da lista é a string 'TIMESTAMP' (x+1 para pular)
    
    # pega o dia da semana correspondente a data acima
    d_weekday = datetime.date.isoweekday(d)

    # transforma a data em uma STRING da mesma
    d = d.strftime('%Y-%m-%d')

    # quebro a string da data e realoco os valores de ANO, MÊS e DIA para as variáveis correspondentes
    d_ano, d_mes, d_dia = d.split('-')

    d_ano_l.append(d_ano)
    d_mes_l.append(d_mes)
    d_dia_l.append(d_dia)
    d_weekday_l.append(d_weekday)

['DAY'] + d_dia_l
['MES'] + d_mes_l
['ANO'] + d_ano_l
['WEEK_DAY'] + d_weekday_l
se = pd.Series(d_dia_l)
file['DAY'] = se
file.to_csv('teste.csv', index = False, header = None)

#
# for x in range(0, size):
    



# https://docs.python.org/2/library/datetime.html#datetime.date.weekday

# date.weekday() 
#    Return the day of the week as an integer, where Monday is 0 and Sunday is 6. For example, date(2002, 12, 4).weekday() == 2, a Wednesday. See also isoweekday().
# date.isoweekday() 
#   Return the day of the week as an integer, where Monday is 1 and Sunday is 7. For example, date(2002, 12, 4).isoweekday() == 3, a Wednesday. See also weekday(), isocalendar().