
###● Discretização - As coordenadas do GPS a fim de manter a funcionalidade d
#algoritmo de Clusterização, precisam ser discretizadas onde vamos definir um
#intervalo de categorização de [-0,9;+0,9] ou([-0,1;+0,1]) para cada coordenada

###● Limpeza dos dados – ​Em nossa base de dados existe um atributo DAYTYPE: (char),
#que identifica a data da corrida informado pelo challenge que possui alguns erros de
#cálculo podendo influenciar no resultado, uma estratégia é validar os dados
#comparando com a base de feriados de portugal
#https://holidays.retira.eu/public-holidays/portugal/

####● Construção de atributos - a base de dados possui um atributo denominado
#MISSING_DATA: (Boolean), que identifica se o caminho está incompleto,
#consequentemente se é necessário prever (classificar) o destino final, o algoritmo
#que pretendemos utilizar é o KNN utilizando da base de treino que contém ~330
#casos de teste, optamos por utilizá-lo pois a demanda de dados é muito alta ~1.7
#milhões de dados e calcular uma árvore de decisão não incremental impacta
#diretamente o algoritmo, devido a perda de conhecimento dado o Delta entre base de
#teste e input. Assumindo assim o risco de alta sensibilidade a outliers do KNN, em
#troca do conhecimento dos dados.

####● Associação de valores numéricos a campos não-numéricos: a fim de possibilitar o
#cálculo de distância, campos não numéricos terão seus valores convertidos em
#números segundo regra específica para cada campo.


####● Normalização das trajetórias: além de cada trajeto ter um comprimento diferente,
#trajetos com a mesma origem e destino podem ter diferentes quantidades de pares
#latitude/longitude. Isto depende do caminho escolhido pelo motorista e do tempo a
#partir do início da viagem em que o classificador fará a previsão (se o motorista
#percorreu uma porcentagem maior da trajetória no momento da análise, a lista terá
#mais pontos.). A fim de aplicar o KNN, as trajetórias devem ser associadas a valores
#numéricos e ser normalizadas a fim de não viciar o cálculo de distâncias utilizado
#pelo algoritmo.