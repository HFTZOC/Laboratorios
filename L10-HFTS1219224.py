print("Semana No. 10: Ejercicio 1")
mes=int(input("Ingrese un numero que se encuentre en el rango de 1 y 12: "))
if mes <1 or mes >12: 
    print("Error: El número ingresado debe estar entre los valores de 1 y 12")
else:
    if mes==1:
        print("mes: enero")
    elif mes==2:
        print("mes: febrero")
    elif mes==3:
        print ("mes: marzo")
    elif mes==4:
        print ("mes: abril")
    elif mes==5:
        print ("mes: mayo")
    elif mes==6:
        print ("mes: junio")
    elif mes==7:
        print ("mes: julio")
    elif mes==8:
        print ("mes: agosto")
    elif mes==9:
        print ("mes: septiembre")
    elif mes==10:
        print ("mes: octubre")
    elif mes==11:
        print ("mes: noviembre")
    elif mes==12:
        print ("mes: diciembre")
    
#Ejercicio 2
print("Semana No. 10: Ejercicio 2")
A=int(input("Ingrese un numero mayor a 0:"))
B=int(input("Ingrese otro numero mayor a 0:"))
C=int(input("Ingrese otro numero mayor a 0:"))
if A>B:
    if A>C:
        print("El numero mayor es:", A)
    else: 
        if A==C:
            print("Los numeros mayores son:", A ,"y",C)
        else:
            print("El numer mayor es:", C )
else: 
        if A==B:
            if A>C:
                print("Los numeros mayores son:", A ,"y", B)
            else:
                if A==C:
                    print("Los tres valores son iguales")
                else: 
                    print("El numero mayor es:", C)
        else: 
            if B>C:
                print("El mayor es:", B)
            else:
                if B==C:
                    print("Los numeros mayores son:", B, "y", C)
                else:
                    print("El numero mayor es:", C)

#Ejercicio 3
