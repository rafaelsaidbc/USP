def fatorial(n):
    fat = 1 #variavel fat recebe o valor 1, porque 1 eh um valor nulo em uma multiplicacao
    while(n > 1): #enquanto n for maior que 1, o laço (while) continua executando
        fat = fat * n #multiplica fat por n
        n = n - 1 #atualiza o n subtraindo 1
    return fat #finalzia o while e atualiza a variavel fat

def testa_fatorial(): #testa a funcao fatorial
    if fatorial(1) == 1:
        print("Funciona para 1")
    else:
        print("Não funciona para 1")

    if fatorial(2) == 2:
        print("Funciona para 2")
    else:
        print("Não funciona para 2")

    if fatorial(0) == 1:
        print("Funciona para 0")
    else:
        print("Não funciona para 0")

    if fatorial(5) == 120:
        print("Funciona para 5")
    else:
        print("Não funciona para 5")
