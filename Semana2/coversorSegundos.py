segundosTotais = int(input("Digite a quantidade de segundos a converter: "))

horas = segundosTotais//3600
minutos = (segundosTotais%3600)//60
segundos = (segundosTotais%3600)%60

print("{} horas, {} minutos, {} segundos.".format(horas,minutos,segundos))