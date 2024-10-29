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
def get_min(my_list):
    num_menor = my_list[0]
    for num in my_list:
        if num_menor <= num:
            num_menor = num
    return num_menor
#max de una lista
def get_max(my_list):
    num_mayor = my_list[0]
    for num in my_list:
        if num > num_mayor:
            num_mayor=num
    return num_mayor



