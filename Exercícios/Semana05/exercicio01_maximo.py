def maximo(x, y):
    if x > y:
        return(x)
    if y > x:
        return(y)
x = int(input("Digite o x: "))
y = int(input("Digite o y: "))
print (maximo(x, y))
