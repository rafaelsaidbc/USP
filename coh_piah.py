import re
 
def le_assinatura():
    """
    A funcao le os valores dos tracos linguisticos do modelo e devolve uma
    assinatura a ser comparada com os textos fornecidos.
    """
    print("Bem-vindo ao detector automático de COH-PIAH.")
 
    tamanho_medio_palavras = float(input("Informe o tamanho medio das palavras: "))
    type_token = float(input("Informe a relação Type-Token: "))
    hapax_legomana = float(input("Informe a Razão Hapax Legomana: "))
    tamanho_medio_sentenca = float(input("Informe o tamanho médio das sentenças: "))
    complexidade_sentenca = float(input("Informe a complexidade das sentenças: "))
    tamanho_medio_frase = float(input("Informe o tamanho medio das frases: "))
 
    return [tamanho_medio_palavras, type_token, hapax_legomana, tamanho_medio_sentenca, complexidade_sentenca, tamanho_medio_frase]
 
def le_textos():
    i = 1
    textos = []
    texto = input("Digite o texto " + str(i) + "(aperte enter para sair):")
    while texto:
        textos.append(texto)
        i += 1
        texto = input("Digite o texto " + str(i) + "(aperte enter para sair):")
    return textos
 
def calcula_assinatura(texto):
    """
    Essa funcao recebe um texto e deve devolver a assinatura
    do texto.
    """
    if type(texto) != list:
        auxiliar = texto
        texto = []
        texto.append(auxiliar)
    for i in texto:
        sentencas = []
        sentencas = separa_sentencas(str(i))  # sent.. = lista comum, ~matriz
        frases = []
        numero_sentencas = 0
        soma_sentencas = 0
        for i in range(len(sentencas)):
            frase_i = separa_frases(str(sentencas[i]))
            frases.append(frase_i)  # frases = matriz, lista de listas
            numero_sentencas += 1
            soma_sentencas = soma_sentencas + len(sentencas[i])
        palavras = []
        numero_total_frases = 0
        soma_frases = 0
        for linha in range(len(frases)):
            for coluna in range(len(frases[linha])):
                palavra_i = separa_palavras(str(frases[linha][coluna]))
                palavras.append(palavra_i)  # palav.. = matriz, lista de listas
                numero_total_frases += 1
                soma_frases = soma_frases + len(str(frases[linha][coluna]))
        matrix_lista = []  # transform.. palavras de matriz para lista
        for linha in range(len(palavras)):
            for coluna in range(len(palavras[linha])):
                matrix_lista.append(palavras[linha][coluna])
        palavras = matrix_lista[:]
        soma_palavras = 0
        total_palavras = 0
        for linha in range(len(palavras)):
            for coluna in range(len(palavras[linha])):
                soma_palavras = soma_palavras + len(str(palavras[linha][coluna]))
            total_palavras += 1
        matriz_assinatura = []
        matriz_assinatura.append(tamanho_medio_palavras(soma_palavras, total_palavras))
        matriz_assinatura.append(type_token(palavras, total_palavras))
        matriz_assinatura.append(hapax_legomana(palavras, total_palavras))
        matriz_assinatura.append(tamanho_medio_sentenca(soma_sentencas, numero_sentencas))
        matriz_assinatura.append(complexidade_sentenca(numero_total_frases, numero_sentencas))
        matriz_assinatura.append(tamanho_medio_frase(soma_frases, numero_total_frases))
    return matriz_assinatura  # matriz, lista de listas dos valores das assina..
 
def tamanho_medio_palavras(soma_palavras, total_palavras):
    if total_palavras != 0:
        tamanho_medio_palavras = soma_palavras / total_palavras
    else:
        tamanho_medio_palavras = 0
    return tamanho_medio_palavras
 
 
def type_token(lista_palavras, total_palavras):
    total_palavras_diferentes = n_palavras_diferentes(lista_palavras)
    if total_palavras != 0:
        type_token = total_palavras_diferentes / total_palavras
    else:
        type_token = 0
    return type_token
 
def hapax_legomana(lista_palavras, total_palavras):
    palavras_unicas = numero_palavras_unicas(lista_palavras)
    if total_palavras != 0:
        hapax_legomana = palavras_unicas / total_palavras
    else:
        hapax_legomana = 0
    return hapax_legomana
 
def tamanho_medio_sentenca(soma_num_cat, numero_setencas):
    if numero_setencas != 0:
        tamanho_medio_sentenca = soma_num_cat / numero_setencas
    else:
        tamanho_medio_sentenca = 0
    return tamanho_medio_sentenca
 
def complexidade_sentenca(numero_total_frases, numero_sentencas):
    if numero_sentencas != 0:
        complexidade_sentenca = numero_total_frases / numero_sentencas
    else:
        complexidade_sentenca = 0
    return complexidade_sentenca
 
 
def tamanho_medio_frase(soma_frases, numero_total_frases):
    if numero_total_frases != 0:
        tamanho_medio_frase = soma_frases / numero_total_frases
    else:
        tamanho_medio_frase = 0
    return tamanho_medio_frase
 
def separa_sentencas(texto):
    """
    A funcao recebe um texto e devolve uma lista das sentencas dentro
    do texto.
    """
    sentencas = re.split(r'[.!?]+', texto)
    if sentencas[-1] == '':
        del sentencas[-1]
    return sentencas
 
def separa_frases(sentenca):
    """
    A funcao recebe uma sentenca e devolve uma lista das frases dentro
    da sentenca.
    """
    return re.split(r'[,:;]+', sentenca)
 
 
def separa_palavras(frase):
    """
    A funcao recebe uma frase e devolve uma lista das palavras dentro
    da frase.
    """
    return frase.split()
 
def numero_palavras_unicas(lista_palavras):
    """
    Essa funcao recebe uma lista de palavras e devolve o numero de palavras
    que aparecem uma unica vez.
    """
    frequencia = dict()
    unicas = 0
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in frequencia:
            if frequencia[p] == 1:
                unicas -= 1
            frequencia[p] += 1
        else:
            frequencia[p] = 1
            unicas += 1
 
    return unicas
 
def n_palavras_diferentes(lista_palavras):
    """
    Essa funcao recebe uma lista de palavras e devolve o numero de palavras
    diferentes utilizadas.
    """
    frequencia = dict()
    for palavra in lista_palavras:
        p = palavra.lower()
        if p in frequencia:
            frequencia[p] += 1
        else:
            frequencia[p] = 1
 
    return len(frequencia)
 
def compara_assinatura(ass_main, matriz_assinatura):
    """
    Essa funcao recebe duas assinaturas de texto e deve devolver o grau de
    similaridade nas assinaturas.
    """
    lista_Sab = []
    soma_mod = 0
    if type(matriz_assinatura[0]) is list:
        for linha in range(len(matriz_assinatura)):
            for coluna in range(len(matriz_assinatura[linha])):
                soma_mod += abs(ass_main[coluna] - matriz_assinatura[linha][coluna])
            Sab = soma_mod / 6
            lista_Sab.append(Sab)
        return lista_Sab
    else:
        for i in range(len(matriz_assinatura)):
            soma_mod += abs(ass_main[i] - matriz_assinatura[i])
        Sab = soma_mod / 6
        return Sab
 
def avalia_textos(textos_main, ass_comparadas):
    """
    Essa funcao recebe uma lista de textos e deve devolver o numero (0 a n-1)
    do texto com maior probabilidade de ter sido infectado por COH-PIAH.
    """
    auxiliar_ass_com = (ass_comparadas[:])
    auxiliar_ass_com.sort()
    for indice in range(len(ass_comparadas)):
        if auxiliar_ass_com[0] == ass_comparadas[indice]:
            copiah = indice
    return copiah
