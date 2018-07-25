#F = P * (1 + J) * T
# Formula valor futuro M = P * ((1 + i) ** n)
#M - montante, valor futuro
#P - valor atual, principal
#i - taxa de juros
#n - meses
#Formula Juros J = M - P
#J - juros

import decimal

valorAtual = 10000
meses = float(input("Digite o período em meses: "))
mesesFloat = meses / 100
juros = 0.08
montante = valorAtual * ((1 + juros) ** mesesFloat)
print(round(montante, 2))
