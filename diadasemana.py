# entra com o timestamp desejado (entrar com o arquivo depois)
# timestamp = input('timestamp: ')

# transforma o timestamp em uma DATA (ANO-MÊS-DIA) -->> DATA = objeto
d = datetime.date.fromtimestamp(int(timestamp))

# pega o dia da semana correspondente a data acima
d_weekday = datetime.date.isoweekday(d)

# transforma a data em uma STRING da mesma
d = d.strftime('%Y-%m-%d')

# quebro a string da data e realoco os valores de ANO, MÊS e DIA para as variáveis correspondentes
d_ano, d_mes, d_dia = d.split('-')

# print dia da semana correspondente
if d_weekday == 1:
    print('Segunda')
elif d_weekday == 2:
    print('Terça')
elif d_weekday == 3:
    print('Quarta')
elif d_weekday == 4:
    print('Quinta')
elif d_weekday == 5:
    print('Sexta')
elif d_weekday == 6:
    print('Sabado')
else:
    print('Domingo')

# checagem de feriados
if d_dia == '01' and d_mes == '01':
    feriado = True
elif d_dia == '24' and d_mes == '04':
    feriado = True
elif d_dia == '01' and d_mes == '05':
    feriado = True
elif d_dia == '31' and d_mes == '05':
    feriado = True
elif d_dia == '10' and d_mes == '06':
    feriado = True
elif d_dia == '15' and d_mes == '08':
    feriado = True
elif d_dia == '05' and d_mes == '10':
    feriado = True
elif d_dia == '01' and d_mes == '11':
    feriado = True
elif d_dia == '01' and d_mes == '12':
    feriado = True
elif d_dia == '08' and d_mes == '12':
    feriado = True
elif d_dia == '25' and d_mes == '12':
    feriado = True
else:
    feriado = False

if feriado == False:
    print('Não é feriado')
else:
    print('É feriado')














# https://docs.python.org/2/library/datetime.html#datetime.date.weekday

# date.weekday()
#    Return the day of the week as an integer, where Monday is 0 and Sunday is 6. For example, date(2002, 12, 4).weekday() == 2, a Wednesday. See also isoweekday().
# date.isoweekday()
#   Return the day of the week as an integer, where Monday is 1 and Sunday is 7. For example, date(2002, 12, 4).isoweekday() == 3, a Wednesday. See also weekday(), isocalendar().