def soma_elementos(lista):
    if len(lista) == 1:
        return lista[0]
    else:
        return lista[0] + soma_elementos(lista[1:])
teste_soma_elementos = [1, 2, 3, 4]
print("O resultado da soma dos elementos da lista é: ", soma_elementos(teste_soma_elementos))
