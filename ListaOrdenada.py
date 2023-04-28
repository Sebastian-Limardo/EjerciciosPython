#funciones

def verificar_lista(lista):
    
    i=0
    
    while i < len(lista)-1 and lista[i] <= lista[i+1] :
        
                              
        i=i+1
        
    if i < len(lista)-1:
        return False
    else:
        return True
    
#programa principal
    
lista1=[]

z = int(input("Ingresar numeros enteros de manera ascendente o descendente. Condición de fin -999: "))

while z != -999:
    lista1.append(z)
    z = int(input("Ingresar numeros enteros de manera ascendente o descendente. Condición de fin -999: "))
    
    
        
    
    
a=verificar_lista(lista1)
print(a)