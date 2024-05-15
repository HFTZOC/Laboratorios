import random 
def LlenarVector(arreglo):
    for i in range (10):
        r=random.randint(1,100)
        arreglo.append(r)
    return arreglo 
def Promedio (arreglo):
    sumatoria=0
    for valor in arreglo:
        sumatoria+=valor
    sumatoria=sumatoria/len(arreglo)
    return sumatoria 
def ParesImpares (arreglo):
    sumapar=0
    sumaimpar=0
    for i in range(len(vector)):
        if i %2==0:
            sumapar+=arreglo[i]
        else:
            sumaimpar+=arreglo[i]
    print ("La suma par es:", sumapar)
    print ("La suma impar es:", sumaimpar)
def ContarParImpar (matriz):
    par=0
    impar=0
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
            if matriz [i][j]%2==0:
                par+=1
            else:
                impar+=1
    print ("La cantida de numeros pares es:", par)
    print ("La cantidad de numeros imparese es: ", impar)
def NumeroMayorMenor (matriz):
    mayor=matriz[0][0]
    menor=matriz[0][0]
    for i in range (len(matriz)):
        for j in range (len(matriz[i])):
             mayor=matriz[i][j]
        else:
            menor=matriz[i][j]
    print ("El valor mayor es:", mayor)
    print ("El valor menor es:", menor)
        
print ("Semana 16: Ejercicio 1")
vector=[]
vector=LlenarVector(vector)
print (vector)
print ("El promedio es:", Promedio(vector))
print ("La longitud del arreglo es:", len(vector))
ParesImpares(vector)

#EJERCICIO 2 

print ("Semana 16: Ejercicio 2")
filas=int(input("Ingrese la cantidad de filas: "))
columnas=int(input("ingrese la cantidad de columnas: "))
matriz=[]
for i in range (filas):
    temp=[]
    for j in range (columnas):
        r=random.randint(0, 1001)
        temp.append(r)
    matriz.append(temp)
print(matriz)
ContarParImpar(matriz)
NumeroMayorMenor(matriz)