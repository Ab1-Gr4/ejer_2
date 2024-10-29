#serie de fibonacci
from operator import truediv


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
#comparar listas
def get_comun(my_list1,my_list2):
    comun=[]
    for elem in my_list1:
        if elem in my_list2:
            if elem not in comun:
                comun.append(elem)
    return comun


#tanque de agua
def get_areaMax(altura):
    left =0
    right=len(altura)-1
    area_max =0
    while left < right:
        distancia=right-left
        area1=min(altura[left],altura[right])*distancia
        area_max=max(area_max,area1)
        if altura[left]<altura[right]:
            left=left+1
        else:
            right=right-1
    return area_max
#conjetura de Goldbach
print("Conjetura de Goldbach ")
n=int(input("ingrese su numero (par mayor a 2)"))
if n<= 2 or n % 2!= 0:
    print("La conjetura de Goldbach solo aplica a numeros pares mayores a 2 ")
else:
    num_prim=[]
    for i  in range(2,n):
        primo = True
        for j in range(2,int(i*0.5)+1):
            if i%j ==0:
                primo = False
                break
        if  primo:
            num_prim.append(i)
    demostrar= False
    for p in num_prim:
        if(n-p) in num_prim:
            print(f"{n} = {p} + {n-p}")
            demostrar = True
            break
    if not demostrar:
        print("no se encontro el par")


