import random

def normaliza_lista(vector):
    '''normaliza a 1 un vector recibido por parametro'''
    n=sum(vector)
    for i in range(len(vector)):
        vector[i]=vector[i]/n

#programa principal
lista=[]

#carga lista aleatoria
elem=random.randint(2,10)
for i in range(elem):
    num=random.randint(-100,100)
    lista.append(num)

print(lista, "\n", sep="")

#llama a la funcion para normalizar la lista
norma=normaliza_lista(lista)
for i in range(len(lista)):
    print("[","%.2f" %(lista[i]), end="]", sep="")
    
#imprime el valor de
lista1=sum(lista)
print("\n", lista1, "\n", sep="")