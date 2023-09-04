import math

print("CALCULADORA DE EQUACAO DO SEGUNDO GRAU")
print("Forma geral: ax² + bx + c = 0")

a = float(input("a: "))
b = float(input("b: "))
c = float(input("c: "))

delta = b*b - 4*a*c

if delta>0:
    print("A equação possui 2 raízes reais diferentes.")
    x1 = (-b - math.sqrt(delta))/(2*a)
    x2 = (-b + math.sqrt(delta))/(2*a)
    print("x1 = {:.2f} e x2 = {:.2f}".format(x1,x2))
elif delta==0:
    print("A equação possui 2 raízes reais iguais.")
    x1 = -b/(2*a)
    print("x = {:.2f}".format(x1))
else:
    print("A equação não possui raízes reais.")