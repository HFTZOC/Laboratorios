print("Semana No. 12: Ejercicio 1\n")
def ObtenerAreaTriangulo():
    base=int(input("Ingrese la base del triangulo\n"))
    altura=int(input("Ingrese la altura del triangulo\n"))
    area=(base*altura)/2
    print("El area de su triangulo es:\n", area,"\n")
def ObtenerAreaCuadrado():
    Lado=int(input("Ingrese el valor del lado de su cuadrado:\n"))
    area=(Lado)*(Lado)
    print("El area de su cuadrado es de: \n", area,"\n")
def ObtenerAreaRectangulo():
    base=int(input("Ingrese la base del rectangulo\n"))
    altura=int(input("Ingrese la altura del rectangulo\n"))
    area=base*altura
    print("El area de su rectangulo es de: \n", area,"\n")
def ObtenerAreaCirculo():
    pi=3.1416
    radio=int(input("Ingrese el valor de su radio:\n"))
    area=pi*((radio)*(radio))
    print("El area de su circulo es de: \n", area,"\n")
menu=0
while menu<=6 and menu>=0:
    menu=int(input("Ingrese un número con la opción con la que desea continuar:\n1. Área de triángulo\n2. Área de cuadrado\n3. Área de rectángulo\n4. Área de círculo\n5. Salir del programa\n"))
    if menu==1:
        ObtenerAreaTriangulo()
    if menu==2:
        ObtenerAreaCuadrado()
    if menu==3:
        ObtenerAreaRectangulo()
    if menu==4:
        ObtenerAreaCirculo()
    if menu==5:
        break
    else:
        print("Ingrese un número adecuado")
print("Semana No. 12: Ejercicio 2\n")
x=0
y=0
def MoverHaciaArriba(x,y):
    y=y+1
    return x, y
def MoverHaciaAbajo(x,y):
    y=y-1
    return x, y
def MoverHaciaLaDerecha(x,y):
    x=x+1
    return x, y
def MoverHaciaLaIzquierda(x,y):
    x=x-1
    return x, y
while menu>0 and menu<6:
    menu=int(input("Ingrese un número con la opción con la que desea continuar:\n1. Sube\n2. Baja\n3. Izquierda\n4. Derecha\n5. Salir\n"))
    if menu==1:
        x, y = MoverHaciaArriba(x,y)
        print("Sus coordenadas actuales son:", x,",",y)
    if menu==2:
        x, y = MoverHaciaAbajo(x,y)
        print("Sus coordenadas actuales son:", x,",",y)
    if menu==3:
        x, y = MoverHaciaLaIzquierda(x,y)
        print("Sus coordenadas actuales son:", x,",",y)
    if menu==4:
        x, y = MoverHaciaLaDerecha(x,y)
        print("Sus coordenadas actuales son:", x,",",y)
    if menu==5:
        print("Coordenadas finales del personaje:", x,",",y)
        break
