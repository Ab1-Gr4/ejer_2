#main.py
def fibonacci(n):
    print("Ejercicio 2 secuencia de Fibonacci")
    print("numeros de la secuencia :")
    a = 0
    b = 1
    c = 1
    res = []
    print("La secuencia es:")
    while c <= num:
        if c == 1:
            res.append(a)
        elif c == 2:
            res.append(b)
        else:
            prox = a + b
            res.append(prox)
            a = b
            b = prox
        c = c + 1
    return res