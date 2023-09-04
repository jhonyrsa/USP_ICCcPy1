def main():
    numero = int(input("Digite um numero: "))
    adjacencia = False
    dividendo=numero
    resto=1
    anterior=dividendo
    while dividendo!=0 and not adjacencia:
        resto = dividendo%10
        dividendo = dividendo//10
        if anterior==resto:
            adjacencia = True
        anterior = resto
    if adjacencia:
        print("O numero {} possui numeros adjacentes iguais.".format(numero)) 
    else:
        print("O número {} não possui números adjacentes iguais.".format(numero))       
main()