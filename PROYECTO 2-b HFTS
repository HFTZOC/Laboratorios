#PROYECTO 2 - HENRY FERNANDO TZOC SOSA - 1219224 
def ColumnasConLetras(columna):
    columnas = {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, 'f': 6, 'g':7, 'h': 8}
    return columnas.get(columna, -1)
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
def MostrarMovimientosValidos(tablero, ft, cNo, ct, letras):
    movimientos = []

    # Movimientos hacia arriba
    fila_actual = ft - 1
    while 1 <= fila_actual <= 8 and tablero[fila_actual][cNo] == pu:
        movimientos.append((fila_actual, cNo))
        fila_actual -= 1
    if 1 <= fila_actual <= 8:
        if tablero[fila_actual][cNo][1] != ct:
            movimientos.append((fila_actual, cNo))
        else:
            print(f"Pieza del mismo equipo ({tablero[fila_actual][cNo][0]}) en {letras[cNo-1]}{fila_actual}.")
    
    # Movimientos hacia abajo
    fila_actual = ft + 1
    while 1 <= fila_actual <= 8 and tablero[fila_actual][cNo] == pu:
        movimientos.append((fila_actual, cNo))
        fila_actual += 1
    if 1 <= fila_actual <= 8:
        if tablero[fila_actual][cNo][1] != ct:
            movimientos.append((fila_actual, cNo))
        else:
            print(f"Pieza del mismo equipo ({tablero[fila_actual][cNo][0]}) en {letras[cNo-1]}{fila_actual}.")
    
    # Movimientos hacia la izquierda
    col_actual = cNo - 1
    while 1 <= col_actual <= 8 and tablero[ft][col_actual] == pu:
        movimientos.append((ft, col_actual))
        col_actual -= 1
    if 1 <= col_actual <= 8:
        if tablero[ft][col_actual][1] != ct:
            movimientos.append((ft, col_actual))
        else:
            print(f"Pieza del mismo equipo ({tablero[ft][col_actual][0]}) en {letras[col_actual-1]}{ft}.")
    
    # Movimientos hacia la derecha
    col_actual = cNo + 1
    while 1 <= col_actual <= 8 and tablero[ft][col_actual] == pu:
        movimientos.append((ft, col_actual))
        col_actual += 1
    if 1 <= col_actual <= 8:
        if tablero[ft][col_actual][1] != ct:
            movimientos.append((ft, col_actual))
        else:
            print(f"Pieza del mismo equipo ({tablero[ft][col_actual][0]}) en {letras[col_actual-1]}{ft}.")
    
    # Mostrar los movimientos válidos para cada dirección
    if movimientos:
        print(f"Movimientos válidos:")
        for movimiento in movimientos:
            fila_m, col_m = movimiento
            if tablero[fila_m][col_m] == pu:
                print(f"Casilla vacía en {letras[col_m-1]}{fila_m}")
            else:
                print(f"Pieza del equipo contrario ({tablero[fila_m][col_m][0]}) en {letras[col_m-1]}{fila_m}")
    else:
        print(f"No hay movimientos válidos.")
ct = input("Escribe el color de tu torre (negro o blanco):\n").lower()
while ct not in ["negro","blanco"]:
    print("solo debes escribir blanco o negro")
    ct = input("Ingrese (negro o blanco):\n")
c = input("Ingrese la columna donde desea colocar la pieza (a-h):\n").lower()
while c not in letras:
    print("Debes escribir una letra desde a hasta h")
    cNo = input("Ingrese la columna (a-h):\n").lower()
cNo = ColumnasConLetras(c) 
ft = int(input("Ingrese la fila (1-8):\n"))
while ft not in [1,2,3,4,5,6,7,8]:
    print("Error! solo numeros de 1 a 8")
    ft = int(input("Ingrese la fila (1-8):\n"))
while ft not in range(1, 9) or cNo == -1:
    print("Posición inválida.")
    cc = input("Ingrese la columna (a-h):\n").lower()
    while c not in letras:
        print("Debes escribir una letra desde a hasta h")
        columnaP = input("Ingrese la columna (a-h):\n").lower()
    cNo = ColumnasConLetras(cc) 
    ft = int(input("Ingrese la fila (1-8):\n"))
    while ft not in [1,2,3,4,5,6,7,8]:
        print("Error! solo numeros de 1 a 8")
        ft = int(input("Ingrese la fila (1-8):\n"))

pu="(                )"
tablero = [[pu for _ in range(9)] for _ in range(9)]
tablero[0][0] = ' / / '
tablero[ft][cNo] = ["Torre", ct]
letras = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
numeros = ['1', '2', '3', '4', '5', '6', '7', '8']
for i in range(1, 9):
    tablero[i][0] = numeros[i-1]

N = int(input("Ingrese el número de piezas que quieres agregar:\n"))
for _ in range(N):
    piezas_de_ajedrez = ["rey", "reina", "torre", "alfil", "caballo", "peon"]
    p = input("Ingrese el tipo de pieza (ejemplo: alfil, peon, torre, etc.):\n")
    while p not in piezas_de_ajedrez:
        print("Debes escribir una pieza correcta")
        p = input("Ingrese el tipo de pieza (ejemplo: alfil, peon, torre, etc.):\n")
    color = input("Ingrese el color deseado (negro o blanco):\n")
    while color not in ["negro","blanco"]:
        print("solo debes escribir blanco o negro")
        color = input("Ingrese el color deseado (negro o blanco):\n")
    columnaP = input("Ingrese la columna (a-h):\n").lower()
    while columnaP not in letras:
        print("Debes escribir una letra desde a hasta h")
        columnaP = input("Ingrese la columna  (a-h):\n").lower()
    fp = int(input("Ingrese la fila  (1-8):\n"))
    while fp not in [1,2,3,4,5,6,7,8]:
        print("Error! solo numeros de 1 a 8")
        filat = int(input("Ingrese la fila(1-8):\n"))
    cP = ColumnasConLetras(columnaP)
    if fp not in range(1, 9) or cP == -1:
        print("Posición inválida.")
    while tablero[fp][cP] != pu:
        print("Error! hay una pieza ahi intenta de nuevo")
        columnaP = input("Ingrese (a-h):\n").lower()
        while columnaP not in letras:
            print("Debes escribir una letra desde a hasta h")
            columnaP = input("Ingrese la columna  (a-h):\n").lower()
        fp = int(input("Ingrese la fila (1-8):\n"))
        while fp not in [1,2,3,4,5,6,7,8]:
            print("Error! solo numeros de 1 a 8")
            filat = int(input("Ingrese la fila (1-8):\n"))
        cP = ColumnasConLetras(columnaP)   
    if tablero[fp][cP] == pu:
        tablero[fp][cP] = [p, color]

# Impresión del tablero
print("  a  b  c  d  e  f  g  h")
for i in range(9):
    for j in range(9):
        print(tablero[i][j], end=' ')
    print()

MostrarMovimientosValidos(tablero, ft, cNo, ct, letras)
