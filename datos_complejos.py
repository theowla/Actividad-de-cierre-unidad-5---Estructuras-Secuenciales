#definimos el diccionario
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}  

#actividad 1
def actividad_1():
    #agregamos valores al diccionario
    precios_frutas['Naranja'] = 1200
    precios_frutas['Manzana'] = 1500
    precios_frutas['Pera'] = 2300

    print(precios_frutas) #imprimimos el diccionario actualizado

#actividad 2
def actividad_2():
    #cambiamos los valores del diccionario
    precios_frutas['Banana'] = 1330
    precios_frutas['Manzana'] = 1700
    precios_frutas['Melón'] = 2800

    print(precios_frutas) #imprimimos el diccionario actualizado


#actividad 3
def actividad_3():
    #creamos una variable con las keys del diccionario
    frutas = precios_frutas.keys()
    print(frutas)  #imprimimos la variable

#actividad 4
#creamos un diccionario
contactos = {}

def lista_contactos(): #funcion para crear los contactos
    for i in range(5): #pedimos 5 contactos y sus numeros
        n = True #definimos n para el loop while
        while n:
            print(f"Contacto N° {i + 1}")
            contacto = input("Contacto: ") #pedimos un contacto
            numero = input("Numero: ") #pedimos su numero

            if contacto.isalpha() and numero.isdigit(): #validamos las variables
                if contacto not in contactos: #si no esta en contactos lo agregamos
                    contactos[contacto] = numero
                    n = False #terminamos el loop
                else:
                    print("Contacto ya registrado")
            else:
                print("Contacto invalido")

def consultar(nombre): #funcion para consultar los contactos
    if nombre in contactos: #si esta en contactos imprimimos su numero
        print(contactos[nombre])
    else:
        print("Este contacto no existe")

#actividad 5

def actividad_5(texto):
    if texto != "": #si no esta vacia la frase continuamos
        frase = texto.split() #lo dividimos mediante los espacios vacios
        dict_frases = {} #creamos un diccionario
        palabras = set(frase) # convertimos a set para tener los valores unicos

        for i in range(len(frase)): #recorremos la frase
            if frase[i] not in dict_frases: #si no esta en el diccionario la agregamos
                dict_frases[frase[i]] = 1    
            else:
                dict_frases[frase[i]] += 1 #si ya esta presente sumamos a su cantidad

        #imprimimos las variables
        print(palabras) 
        print(dict_frases)
    else:
        print("Texto vacio")

#actividad 6
def actividad_6():
    #definimos el diccionario
    alumnos = {
        "Sofia": (10, 9, 8),
        "Luis": (6, 7, 7)
    }

    for key in alumnos: #recorremos alumnos cada key en el diccionario 
        promedio_alumno = sum(alumnos[key]) #juntamos todas las notas y las sumamos son sum()
        print(f"{key}: {(promedio_alumno / 3):.2f}") #calculamos y imprimimos el promedio a la vez

#actividad 7
#definimos la lista
asistencias = ["Ana", "Luis", "Ana", "Maria", "Luis", "Pedro", "Ana"]

def actividad_7(asistencias):

    dict_asistencias = {} #creamos un diccionario
    empleados = set(asistencias) #agregamos cada empleado unico a una lista

    for i in range(len(asistencias)): #recorremos asistencias
        if asistencias[i] not in dict_asistencias: #si no esta presente lo sumamos al diccionario
            dict_asistencias[asistencias[i]] = 1    
        else:
            dict_asistencias[asistencias[i]] += 1  #si esta presente le sumamos 1 a su cantidad

    #imprimimos las variables
    print(asistencias)
    print(empleados)
    print(dict_asistencias)

#ejercicio 8
def actividad_8():
    #creamos un diccionario 
    productos = {"martillo": 10, "destornillador": 1}

    #imprimimos las opciones
    print("consultar stock: 1")
    print("agregar unidades al stock: 2")
    print("agregar producto: 3")
    print("Salir: 4") #agrege una salida para poder usar multiples veces el programa antes de salir

    while True:
        opcion = input("Opcion: ") #pedimos una opcion
        if opcion.isdigit(): #validamos la opcion
            opcion = int(opcion) #convertimos a int

            if opcion == 4: #opcion de salida previa a pedir el producto
                return False

            producto = input("producto: ").lower() #pedimos y estandarizamos el producto

            if producto.isalpha(): #validamos el producto
                if opcion == 1:
                    if producto in productos: #si el producto esta en el diccionario imprimimos su stock
                        print(f"{producto}: {productos[producto]}")
                    else:
                        print("Este producto no existe.")
                elif opcion == 2:
                    if producto in productos: #si el producto esta en el diccionario pedimos la cantidad a sumar
                        cantidad = input("Cantidad a agregar a stock: ")
                        if cantidad.isdigit(): #validamos la cantidad
                            cantidad = int(cantidad) #convertimos a int
                            if cantidad > 0: #vemos que sea positiva la cantidad
                                productos[producto] += cantidad #la sumamos a stock
                                print(f"Se sumó {cantidad} al stock de {producto}") #mensaje de confirmacion
                            else:
                                print("Error: Tiene que sumar existencias")
                        else:
                            print("cantidad invalida")                    
                    else:
                            print("Este producto no existe.")
                elif opcion == 3:
                    if producto not in productos: #si el producto no esta en el diccionario lo agregamos
                        productos[producto] = 0
                    else:
                        print("Este producto ya existe.")
                else:
                    print("opcion invalida")
            else:
                print("Producto invalido")            
        else:
            print("Opcion tiene que ser un numero")   
#actividad 9
def activad_9():
    #definimos el diccionario
    agenda = {
        ("lunes", "10:00"): "Reunión",
        ("martes", "15:00"): "Clase de inglés"
    }

    #pedimos dia y hora de la agenda
    consulta_dia = input("Dia: ").lower()
    consulta_hora = input("Horario: ")

    consulta = (consulta_dia, consulta_hora) #covertimos a tupla

    if consulta_hora and consulta_dia: #validamos que ambos input no esten vacios
        if consulta in agenda: #si esta en la agenda imprimimos que hay en esa fecha
            print(agenda[consulta])
        else:
            print("No existe nada en agenda para esa fecha.")
    else:
        print("Fecha/Dia invalido.")

#actividad 10
def actividad_10():
    #definimos los diccionarios
    original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
    invertido = {}

    for key in original: #recorremos el diccionario por cada key
        value = original[key] #guardamos su valor
        invertido[value] = key #sumamos al diccionario invertido las variables

    #imprimimos los diccionarios
    print(original)
    print(invertido)

actividad_1()
actividad_2()
actividad_3()
#actividad 4
lista_contactos()
consultar(input("Contacto a consultar: "))
#
actividad_5(input("frase: "))
actividad_6()
actividad_7(asistencias)
actividad_8()
activad_9()
actividad_10()