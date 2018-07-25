def remove_repetidos(lista):
    lista1 = []
    for n in lista:
        if n not in lista1:
            lista1.append(n)
    lista1.sort()
    return lista1
lista = [1, 2, 3, 4, 2, 3, 5, 6, 7, 5, 8, 8, 8, 9]
lista = remove_repetidos(lista)
print(lista)
