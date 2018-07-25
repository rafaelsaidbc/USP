sequencia = []
while True:
    num = int(input("Digite um numero para a lista: "))
    if num != 0:
        sequencia.append(num)
    else:
        break
for i in sequencia[::-1]:
    print(i)
