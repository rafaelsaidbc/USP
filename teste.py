def maior_elemento(lista):
    maximo = lista[0]
    for num in lista:
        if maximo < num:
            maximo = num
    return maximo
teste_maximo = [1, 2, 3, 9, 5, 7, 6, 4, 8]
print(maior_elemento(teste_maximo))
