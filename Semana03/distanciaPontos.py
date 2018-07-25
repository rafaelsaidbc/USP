import math

x1 = int(input("Digite a coordenada do eixo x para o primeiro ponto: "))
y1 = int(input("Digite a coordenada do eixo y para o primeiro ponto: "))
x2 = int(input("Digite a coordenada do eixo x para o segundo ponto: "))
y2 = int(input("Digite a coordenada do eixo y para o segundo ponto: "))
distancia = math.sqrt(((x2-x1)**2) + ((y2-y1)**2))
if distancia >= 10:
    print("longe")
else:
    print("perto")
