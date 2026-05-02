#Ejercicio 1
print("#Ejercicio 1.")
notas = [3,4,5,7,5,8,2,10,2,10] #declaramos la lista

for i in range(len(notas)): #imprimimos la lista item por item
    print(notas[i], end=" ")
print("")
promedio = (sum(notas) / len(notas)) #calculamos promedio
mayor = notas[0] #declaramos variables mayor y menor
menor = notas[0]

for i in range(len(notas)): #recorremos las notas y comparamos con el numero mas grande encontrado y el mas pequeño
    if notas[i] > mayor:
        mayor = notas[i]
    if notas[i] < menor:
        menor = notas[i]

#imprimimos las variables
print(f"Nota Promedio: {promedio}.")
print(f"Nota mayor: {mayor}.")
print(f"Nota menor: {menor}.")

#Ejercicio 2
print("\n#Ejercicio 2.")
productos = [] #inicializamos la lista

for i in range(5): #pedimos 5 veces un numero
    while True:
        producto = input(f"Ingrese el producto N° {i+1}: ")
        if producto != (""): #si producto no esta vacio lo agregamos a la lista
            productos.append(producto)
            break
        else: 
            print("Error: nombre de producto invalido")

productos = sorted(productos) #ordenamos la lista 

for i in range(len(productos)):# imprimimos la lista item por item
    print(productos[i], end=" ")
print("")

while True:
    eliminar = input("¿Que producto desea eliminar?: ") #pedimos el producto a eliminar
    if eliminar != (""): #validamos el input del usuario
        break
    else:
        print("Error: ningun elemento a eliminar.")

if eliminar in productos: #si el producto se encuentra en la lista lo removemos
    print(f"Producto {eliminar} eliminado de la lista.")
    productos.remove(eliminar)

    for i in range(len(productos)): #devolvemos la lista corregida
        print(productos[i], end=" ")
    print("")
else:
    print(f"Error: {eliminar} no existe en la lista.") #en el caso que no este en la lista devolvemos error

#Ejercicio 3
print("\n#Ejercicio 3.")
#inicializamos las variables y importamos random para que sea 100% aleatorio 
import random
numeros = []
par = []
impar = []

for i in range(15): #sumamos 15 numeros aleatorios entre 1-100 a la lista
    numeros.append(random.randint(1, 100))


#recorremos la lista numeros
for i in range(len(numeros)):
    #vemos si el resto de la division por 2 da 0 (par)
    if numeros[i] % 2 == 0:
        par.append(numeros[i])
    #en el caso que sea otro numero (impar)
    else:
        impar.append(numeros[i])

for i in range(len(numeros)): #devolvemos la lista 
    print(numeros[i], end=" ")
print("")

#imprimimos la cantidad de elementos en cada uno
print(f"Cantidad de numeros impar: {len(impar)}")
print(f"Cantidad de numeros par: {len(par)}")

#Ejercicio 4
print("\n#Ejercicio 4.")

#inicializamos las variables
datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]
datosNoRepetidos = [] 

#cada elemento nuevo en la segunda lista se suma, los que se repitan quedan afuera de ella
for i in range(len(datos)):
    if datos[i] not in datosNoRepetidos:
        datosNoRepetidos.append(datos[i])

print("Datos no repetidos:")

for i in range(len(datosNoRepetidos)): #devolvemos la lista sin repetidos
    print(datosNoRepetidos[i], end=" ")
print("")

#Ejercicio 5
print("\n#Ejercicio 5.")

#inicializamos la lista de estudiantes
estudiantes = ["Pedro", "Jorge", "Esteban", "Nicolas", "Carlos", "Martin", "Felipe", "Manuel"]

#imprimimos la lista de estudiantes
for i in range(len(estudiantes)):
    print(estudiantes[i], end=" ")
print("")

while True:
    decision = input("¿Borrar o agregar alumnos? (B/A): ") #preguntamos al usuario la que accion tomara
    if decision.isalpha():
        decision = decision.upper()
        if decision != "B" and decision != "A": #validamos el input del usuario
            print("Error: Decision invalida.")
        else:
            break
    else:
        print("Error: Decision nula.")

while True: #preguntamos el nombre del alumno al que se borrara/agregara
    nombre = input("Nombre del Alumno: ")
    if nombre.isalpha(): #validamos el nombre
        nombre = nombre.title()

        #dependiendo de la accion elegida al principio se elimina o se agrega de la lista
        if decision == "B":
            if nombre in estudiantes: #verificamos que este en la clase
                estudiantes.remove(nombre)
                break
            else:
                print("Error: este alumno no esta en esta clase.")
        elif decision == "A":
            estudiantes.append(nombre)
            break
    else:
        print("Error: Nombre invalido.")

for i in range(len(estudiantes)): #imprimimos la lista actualizada
    print(estudiantes[i], end=" ")
print("")

#Ejercicio 6
print("\n#Ejercicio 6.")

#inicializamos las variables
numeros = [1, 2, 3, 4, 5, 6, 7]
numeros = [numeros[-1]] + numeros[:-1]

for i in range(len(numeros)): #imprimimos la lista de numeros modificada
    print(numeros[i], end=" ")   
print("")

#Ejercicio 7
print("\n#Ejercicio 7.")

#inicializamos las variables
minima = 0
maxima = 0
max_amplitud = 0
semana = [[18, 25], 
          [17, 23], 
          [22, 27], 
          [22, 25], 
          [23, 27], 
          [24, 28], 
          [26, 29] 
          ]

for i in range(len(semana)):
    amplitud = 0 #reiniciamos la amplitud del dia
    minima += semana[i][0] #sumamos la temperatura minima al total semanal
    maxima += semana[i][1] #sumamos la temperatura maxima al total semanal
    amplitud = semana[i][1] - semana[i][0] #calculamos la amplitud del dia

    if amplitud > max_amplitud: #si la amplitud es la mas alta registrada, actualizamos max_amplitud
        max_amplitud = amplitud
        dia_amplitud = i + 1 #guardamos el numero del dia en que se registro

#calculamos los promedios de minima y maxima de la semana
minima = minima / len(semana)
maxima = maxima / len(semana)

#imprimimos los resultados
print(f"Promedio de temperatura minima: {minima:.1f}")
print(f"Promedio de temperatura maxima: {maxima:.1f}")
print(f"Maxima amplitud termica: dia N° {dia_amplitud} con {max_amplitud}°C de diferencia.")

#Ejercicio 8
print("\n#Ejercicio 8.")

#inicializamos las variables
estudiantes = [
    [3, 6, 7],
    [6, 8, 9],
    [8, 3, 9],
    [10, 10, 10],
    [2, 6, 6],
]
promedio = 0
promedio_materia = [0, 0, 0]

for i in range(5):
    for j in range(3):
        promedio += estudiantes[i][j] #sumamos las notas del estudiante
        promedio_materia[j] += estudiantes[i][j] # sumamos las notas de la materia

    promedio = promedio / 3 #calculamos el promedio por estudiante
    print(f"Promedio estudiante N° {i + 1}: {promedio:.2f}") #imprimimos el mismo
    promedio = 0 #reiniciamos la variable para el proximo alumno

print("")

#calculamos y imprimimos los promedios por materia al mismo tiempo
for i in range(3):
    print(f"Promedio materia N° {i + 1}: {(promedio_materia[i] / 5):.2f}")

#Ejercicio 9
print("\n#Ejercicio 9.")

#inicializamos las variables
ta_te_ti = [
    ["-", "-", "-"],
    ["-", "-", "-"],
    ["-", "-", "-"]
    ]
turno = "X"

for i in range(9):
    while True:
        #pedimos fila y columna al usuario
        jugador_fila = input("Fila: ")
        jugador_col = input("Columna: ")

        if jugador_col.isdigit() and jugador_fila.isdigit() and int(jugador_col) in [1,2,3] and int(jugador_fila) in [1,2,3]: #validamos los inputs
            jugador_col, jugador_fila = int(jugador_col), int(jugador_fila) #convertimos a int los inputs

            if ta_te_ti[jugador_fila - 1][jugador_col - 1] == "-": #si se encuentra vacio sumamos X/O segun el turno
                ta_te_ti[jugador_fila - 1][jugador_col - 1] = turno

                if turno == "X": #cambiamos de turno
                    turno = "O"
                else:
                    turno = "X"

                for i in range(3): #imprimimos el tablero
                    for j in range(3):
                        print(ta_te_ti[i][j], end=" ")
                    print("")
                break
            else:
                print("Error: posicion invalida.")
        else:
            print("Error: Valor invalido.")

#Ejercicio 10
print("\n#Ejercicio 10.")

#inicializamos las variables
ventas = [
    [0, 2, 1, 3],
    [1, 0, 2, 4],
    [0, 1, 0, 1],
    [2, 4, 2, 3],
    [3, 5, 4, 2],
    [1, 2, 4, 2],
    [0, 2, 3, 0]
]

total_dia_mayor_ventas = 0
dia_mayor_ventas = 0
total_productos_vendidos = [0] * 4
total_vendido = 0

for i in range(7):
    total_vendido = 0 #reiniciamos la variable

    for j in range(4): #sumamos hacia el total por dia y de productos
        total_vendido += ventas[i][j]
        total_productos_vendidos[j] += ventas[i][j]

    if total_vendido > total_dia_mayor_ventas: #verificamos si el total es mas grande que el maximo total anterior 
        total_dia_mayor_ventas = total_vendido #cambiamos de maximo total
        dia_mayor_ventas = (i + 1) #registramos que dia fue

#inicializamos variables
total_producto_mas_vendido = 0
producto_mas_vendido = 0

for i in range(4): #imprimimos el total por producto
    print(f"Ventas del producto N° {i + 1}: {total_productos_vendidos[i]} ventas")

    if total_producto_mas_vendido < total_productos_vendidos[i]: #verificamos cual es el producto con mas ventas
        total_producto_mas_vendido = total_productos_vendidos[i] #actualizamos cual es el producto mas vendido
        producto_mas_vendido = (i + 1) #guardamos el numero del producto

#imprimimos los resultados
print("")      
print(f"El producto N° {producto_mas_vendido} fue el mas vendido.")
print(f"El dia N° {dia_mayor_ventas} contiene las mayores ventas con {total_dia_mayor_ventas} ventas.")

#Ejercicio 11
print("\n#Ejercicio 11.")

#inicializamos las variables
estudiantes = ["Pedro", "Jorge", "Esteban", "Nicolas", "Carlos", "Martin", "Felipe", "Manuel", "Lucia", "Ana"]
presente = False 

while True:
    nombre = input("Nombre: ") #pedimos un nombre al usuario

    if nombre.isalpha(): #validamos el input
        nombre = nombre.title() #estandarizamos el nombre
        break
    else:
        print("Error: valor invalido.")

#verificamos si el estudiante esta presente y donde se encuentra en la lista
for i in range(len(estudiantes)):
    if estudiantes[i] == nombre:
        presente = True
        print(f"{nombre} esta en la posicion N° {i + 1} de la lista.")
        break

#en el caso de su ausencia en la lista lo aclaramos
if not presente:
    print(f"{nombre} no esta en la lista.")
    
#Ejercicio 12
print("\n#Ejercicio 12.")

#inicializamos la lista
numeros = []

#pedimos 8 veces un numero
for i in range(8):
    while True:
        input_numero = input(f"Ingrese un numero {i + 1}/8: ")
        if input_numero.isdigit(): #validamos el numero
            numeros.append(int(input_numero)) #convertimos a integer
            break
        else:
            print("Error: valor invalido")

#imprimimos la lista original
for i in range(len(numeros)):
    print(numeros[i], end=" ")
print("")

#ordenamos la lista menor a mayor
numeros_menor_mayor = sorted(numeros)

#imprimimos la lista ordenada menor a mayor
for i in range(len(numeros_menor_mayor)):
    print(numeros_menor_mayor[i], end=" ")
print("")

#damos la vuelta a la lista
numeros_menor_mayor.reverse()

#imprimimos la lista mayor a menor (el nombre de la variable no coincide ya que reverse() devuelve el resultado a la lista original)
for i in range(len(numeros_menor_mayor)):
    print(numeros_menor_mayor[i], end=" ")
print("")

#Ejercicio 13
print("\n#Ejercicio 13.")

#inicializamos la lista
puntajes = [450, 1200, 875, 990, 300, 1500, 640]
#ordenamos la lista
puntajes = sorted(puntajes)

#imprimimos el ultimo numero de la lista y el primero (al estar ordenada es el mas alto y el mas bajo respectivamente)
print(f"Puntaje mas alto: {puntajes[-1]}.\nPuntaje mas bajo: {puntajes[0]}.")
#damos la vuelta a la lista
puntajes.reverse()

#imprimimos la lista de mayor a menor
print(f"Puntajes de mayor a menor:")
for i in range(len(puntajes)):
    print(puntajes[i], end=" ")
print("")

#usamos index() para buscar su lugar en el ranking
print(f"990 se encuentra en la posicion N° {puntajes.index(990) + 1}.")

