def main():
    print("Digite uma sequencia de numeros, terminada por 1")
    multiIterada = 1
    valor = 2
    while valor!=1:
        valor = float(input("Digite um valor: "))
        multiIterada = multiIterada*valor
    print("M = {}".format(multiIterada))
main()