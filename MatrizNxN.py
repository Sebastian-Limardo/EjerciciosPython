import random

def rellenar_matriz_al_azar_1(matriz):
    '''esta funcion rellena una matriz cuadrada con numeros al azar diferentes del intervalo [0;N**2),
        esto lo hace mediante la ayuda de una lista auxiliar que almacena los numeros que ya fueron utilizados '''
    N=len(matriz)
    lista_aux=[]
    
    for i in range(N):
        for j in range(N):
            
            num=random.randint(0, N**2-1)
            while num in lista_aux:
                num=random.randint(0, N**2-1)
                
            matriz[i][j]= num
            lista_aux.append(num)
                            
def rellenar_matriz_al_azar_2(matriz):
    '''esta funcion rellena una matriz cuadrada con numeros al azar diferentes del intervalo [0;N**2),
        esto lo hace mediante el recorrido de la matriz(la parte que ya fue procesada solamente)'''
    N=len(matriz)

    for i in range(N):
        for j in range(N):
            
            num= random.randint(0, N**2-1)
            k=0
             
            while k<i:
                if num in matriz[k]:
                    num=random.randint(0, N**2-1)
                    k=0
                    continue
                if num in matriz[i][:j]:
                    num=random.randint(0, N**2-1)
                    k=0
                    continue
                k+=1
            
            else:                                 
                matriz[i][j]= num
                
def mostrar_mat(mat):
    for fila in mat:
        for elem in fila:
            print("%3d"%elem, end=" ")
        print()

#Programa Principal y Pruebas
      
N=int(input("Ingrese N de la matriz tamaño NxN: "))
matriz_prueba1= [[0]*N for i in range(N)]
matriz_prueba2= [[0]*N for i in range(N)]

rellenar_matriz_al_azar_1(matriz_prueba1)
rellenar_matriz_al_azar_2(matriz_prueba2)

mostrar_mat(matriz_prueba1)
print()
mostrar_mat(matriz_prueba2)

    