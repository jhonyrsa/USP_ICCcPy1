import math

a = float(input())
b = float(input())
c = float(input())

delta = b**2 - 4*a*c

if delta==0:
    raiz = (-b)/(2*a)
    print("a raiz desta equação é {:.1f}".format(raiz))
elif delta>0:
    raiz1 = (-b - math.sqrt(delta))/(2*a)
    raiz2 = (-b + math.sqrt(delta))/(2*a)
    if raiz1<raiz2:
        print("as raízes da equação são {:.1f} e {:.1f}".format(raiz1, raiz2))
    else:
        print("as raízes da equação são {:.1f} e {:.1f}".format(raiz2, raiz1))
else:
    print("esta equação não possui raízes reais")