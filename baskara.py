import math

def delta(a, b, c): #define uma função delta
    return b ** 2 - 4 * a * c #retorna o resultado desse problema

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

if delta() == 0:
    raiz1 = (-b + math.sqrt(delta)) / (2 * a)
    print("A única raiz é: ", raiz1)
else:
    if delta < 0:
        print("Esta equação não possui raízes reais")
    else:
        raiz1 = (-b + math.sqrt(delta)) / (2 * a)
        raiz2 = (-b - math.sqrt(delta)) / (2 * a)
        if raiz1 < raiz2:
            print("A primeira raiz é: ", raiz1)
            print("A segunda raiz é: ", raiz2)
        else:
            print("A primeira raiz é: ", raiz2)
            print("A segunda raiz é: ", raiz1)
