def ehPrimo(k):
    if (((k % 2 == 0) or (k % 3 == 0) or (k % 5 == 0)) and not ((k == 3) or (k == 2) or (k == 5))):
        return False
    else:
        return True
def maior_primo(k):
    while (1 < k):
        if (ehPrimo(k)):
            return k
        k = k - 1
