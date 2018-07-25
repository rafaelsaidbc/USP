def vogal (caractere) :
  caractere = caractere.lower()
  if caractere == "a" or caractere == "e" or caractere == "i" or caractere == "o" or caractere == "u":
    return True
  else:
    return False
# Programa começa
entrada = input ("Digite um caractere: ")
ehVogal = vogal(entrada)
print(ehVogal)
