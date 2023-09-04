segundosTotais = int(input("Por favor, entre com o número de segundos que deseja converter: "))

dias = segundosTotais//86400
horas = (segundosTotais%86400)//3600
minutos = ((segundosTotais%86400)%3600)//60
segundos = ((segundosTotais%86400)%3600)%60

print("{} dias, {} horas, {} minutos e {} segundos.".format(dias,horas, minutos,segundos))