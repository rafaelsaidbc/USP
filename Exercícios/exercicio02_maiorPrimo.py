def éPrimo(k):
    while (1 < k):
        if (éPrimo(k)):
            return k
        k = k - 1
def maior_primo(k >= 2):
    if (((k % 2 == 0) or (k % 3 == 0) or (k % 5 == 0)) and not ((k == 3) or (k == 2) or (k == 5))):
        return False
    else:
        return True
