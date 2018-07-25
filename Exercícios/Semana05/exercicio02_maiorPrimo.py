def primo(n):
    if (((n % 2 == 0) or (n % 3 == 0) or (n % 5 == 0)) and not ((n == 3) or (n == 2) or (n == 5))):
        return False
    else:
        return True
def primo_maior(n):
    while (1 < n):
        if (primo(n)):
            return n
        n = n - 1
n = int(input("Digite o n: "))
print(primo_maior(n))
