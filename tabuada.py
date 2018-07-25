linha = 1
coluna = 1
while linha <= 10:
    while coluna <= 10:
        print(linha * coluna, end = "\t") #end = "\t" faz uma tabulação entre os resultados
        coluna = coluna + 1
    linha = linha + 1
    print() #mudar de linha
    coluna = 1

