def MinMax(temperaturas):
    print("A menor temperatura do mês foi: ", minima(temperaturas), "ºC.")
    print("A maior temperatura do mês foi: ", maxima(temperaturas), "ºC.")

def minima(temps):
    min = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] < min:
            min = temps[i]
        i = i + 1
    return min

def maxima(temps):
    max = temps[0]
    i = 1
    while i < len(temps):
        if temps[i] > max:
            max = temps[i]
        i = i + 1
    return max

#funcao dos testes
def teste_minima(temp, valor_esperado):
    valor_calculado = minima(temp)
    if valor_calculado != valor_esperado:
        print("Valor errado para array ", temp)
        print("Valor esperado: ", valor_esperado, ". Valor calculado: ", valor_calculado)

def teste_maxima(temp, valor_esperado):
    valor_calculado = maxima(temp)
    if valor_calculado != valor_esperado:
        print("Valor errado para array ", temp)
        print("Valor esperado: ", valor_esperado, ". Valor calculado: ", valor_calculado)
        
#testes
def testa_minima():
    print("Iniciando testes")
    teste_minima([0], 0)
    teste_minima([0, 0, 0, 0, 0, 0, 0, 0, 0], 0)
    teste_minima([0, 1, 2, 3, 4, 5, 6, 7], 0)
    teste_minima([21, 30, 32, 14, 17, 19, 20, 22, 25, 14, 19], 14)
    teste_minima([-2, 10, 14, 5, 7, -5, 0, -8], -8)
    print("Finalizando testes")

def testa_maxima():
    print("Iniciando testes")
    teste_maxima([0], 0)
    teste_maxima([0, 0, 0, 0, 0, 0, 0, 0, 0], 0)
    teste_maxima([0, 1, 2, 3, 4, 5, 6, 7], 7)
    teste_maxima([21, 30, 32, 14, 17, 19, 20, 22, 25, 14, 19], 32)
    teste_maxima([-2, 10, 14, 5, 7, -5, 0, -8], 14)
    print("Finalizando testes")
    
