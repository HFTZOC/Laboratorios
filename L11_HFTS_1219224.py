#Henry Fernando Tzoc Sosa - 1219224
print("Actividad No. 02 - Serie A")
print()
N=0
while N<=0:
    N=int(input("Ingrese un número N mayor que 0 "))
    if N<=0:
        print("El número ingresado debe ser mayor a 0 ") 
        print()
print("Serie A = (1 / 1) + (1 / 2) + (1 / 3) + … + (1 / N)")
a1=0
resultadoa=0
a2=0
resultadob=0
for i in range(N):
    a1 += 1
    c1 = 1/a1
    resultadoa= resultadoa + c1
    a2 += 1
    c2 = 1/(2**a2)
    resultadob=resultadob + c2
print("El resultado de (1/1)+(1/2)+(1/3)+...+(1/",N, " es", resultadoa)
print()
print("Serie B = (1 / 2^1) + (1 / 2^2) + (1 / 2^3) + … + (1 / 2^N)")
print("El resultado de (1 / 2^1) + (1 / 2^2) + (1 / 2^3) + … + (1 / 2^",N," es", resultadob)
print()
print("Serie C")
x=int(input("Ingrese un numero x entero que sea mayor a 0 "))
while x<=0:
    x=int(input("Ingrese un numero x entero que sea mayor a 0 "))
    if x<=0:
        print("El número ingresado debe ser mayor a 0 ")
a=int(input("Ingrese un número a entero que sea mayor a 0 "))
while a<=0:
    a=int(input("Ingrese un número a entero y mayor a 0 "))
    if a<=0:
        print("El numero ingresado debe ser mayor a 0")
n=int(input("Ingrese un número n entero que sea mayor a cero "))
while n<=0:
    n=int(input("Ingrese un número n entero que sea mayor a cero "))
    if n<=0:
        print("El numero ingresado debe ser mayor a 0")
resultadoc=0
for i in range(n):
    k=0
    k=+1
    c1=(x**k)*(a**(n-k))
    resultadoc= resultadoc + c1 
print("El resultado de la sumatoria del inciso c es ", resultadoc)

    




