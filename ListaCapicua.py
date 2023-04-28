#TP2 - EJERCICIO 1
'''Desarrollar cada una de las siguientes funciones y escribir un programa que
permita verificar su funcionamiento imprimiendo la lista luego de invocar cada funcion.'''

import random

# a - Cargar una lista con numeros al azar de cuatro digitos. La cantidad de elementos tambien sera un numero al azar de dos digitos

def funcion_A():
    largo = random.randint(10,99)
    lista = []
    for i in range(largo):
        a = random.randint(1000,9999)
        lista.append(a)
    return lista

# B - Calcular y devolver la suma de todos los elementos de la lista anterior

def funcion_B(lista):
    return sum(lista)

def funcion_B_primitiva(lista):
    sumatoria = 0
    for i in range(len(lista)):
        sumatoria += lista[i]
    return sumatoria

#C - Eliminar todas las apariciones de un valor de la lista anterior

def funcion_C(x,lista):
    while (x in lista) == True:
        lista.remove(x)
    return lista

def funcion_C_primitiva(x,lista):
    for i in range(len(lista)):
        if lista[i] == x:
            lista.pop(i)
    return lista

#D - Determinar si el contenido de una lista es capicua, sin usar listas auxiliares

def funcion_D(lista):
    '''Devuelve True si la lista es capicua, False si no'''
    capicua = True
    for i in range(len(lista)//2):
        if lista[i] != lista[-(i+1)]:
            capicua = False
            break
    return capicua

'''PROGRAMA PRINCIPAL'''

x = funcion_A()

print("Lista Original: \n",x)
print("Suma de Elementos: \n",funcion_B(x))

eliminar_nro = int(input("Ahora probemos eliminar un numero de la lista; Que numero eliminamos? "))

funcion_C(eliminar_nro,x)

print("Nueva lista; \n",x) #Esto lo podemos hacer porque una lista es mutable

if funcion_D(x) == True:
    print("Es una lista capicua")
else:
    print("No es una lista capicua")















        
