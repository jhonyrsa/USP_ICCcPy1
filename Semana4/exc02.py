def main():
    numero = int(input("Digite um numero: "))
    adjacencia = False
    dividendo=numero
    resto=1
    anterior=dividendo%10
    dividendo = numero//10
    while dividendo!=0 and not adjacencia:
        resto = dividendo%10
        if anterior==resto:
            adjacencia = True
        anterior = resto
        dividendo = dividendo//10
    if adjacencia:
        print("sim") 
    else:
        print("não")       
main()