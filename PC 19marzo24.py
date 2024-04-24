#PROGRAMA PARA REALIZAR SUMATORIAS
contador=1
sumatoria=0
while contador<=15:
    print(contador)
    sumatoria+=contador
    contador+=1
print(sumatoria)
################################################################################################################
print("Semana No 11: Ejercicio 1")

N=0
while N<=0:
    N=int(input("Ingrese un numero mayor que 0: "))
    if N<=0:
        print("El numero debe ser mayor a 0:")
        print()

A=0
B=1
C=0
i=2
resultado=""
resultado+=str(A)
if N>1:
    resultado+=(","+str(B))
    while i<N:
        C=A+B
        resultado+=(","+str(C))
        A=B
        B=C
        i=i+1
    print(resultado)
else:
    print(resultado)