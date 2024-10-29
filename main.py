def fibonacci(n):
    print("Ejercicio 2 secuencia de Fibonacci")
    num = int(input("Introduce la cantidad de números de la secuencia que deseas: "))
    print("numeros de la secuencia :", num)
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
