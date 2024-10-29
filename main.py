def fibonacci(n):
    print("Ejercicio 2 secuencia de Fibonacci")
    print("numeros de la secuencia :")
    a = 0
    b = 1
    c = 1
    res = []
    print("La secuencia es:")
    while c <= n:
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

#min de una lista
#prueba entrada de datos en una lista
elementos = input("introduce numeros (separados por comas):")
mi_lista = [int(num) for num in elementos.split(',')]
print("la lista es:", mi_lista)
num_menor = min(mi_lista)
print("El valor minimo es:",num_menor)