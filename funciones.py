
def imprimir_hola_mundo():
    print("hola mundo") #devuelve hola mundo

def saludar_usuario(nombre):
    return(f"Hola {nombre}!") #toma el argumento de la funcion y devuelve el mensaje

def informacion_personal(nombre, apellido, edad, residencia):
    edad = int(edad)
    print(f"Soy {nombre} {apellido} tengo {edad} años y vivo en {residencia}") #toma los argumentos de la funcion y devuelve el mensaje

def calcular_area_circulo(radio):
    import math
    radio = float(radio) #convertimos a float
    area = (math.pi * (radio ** 2)) #calculamos el area con area = Pi X (radio a la potencia 2)
    return(f"Area del circulo: {area:.2f}")

def calcular_perimetro_circulo(radio):
    import math
    radio = float(radio) #convertimos a float
    perimetro = ((2 * math.pi) * radio) #calculamos el perimetro con perimetro = (2 X Pi) X radio
    return(f"Perimetro del circulo: {perimetro:.2f}")

def segundos_a_horas(segundos):
    segundos = float(segundos) #convertimos a float para mas precision
    horas = (segundos / 3600) #dividimos por la cantidad de segundos en una hora
    return(f"Cantidad de horas: {horas:.2f}")

def tabla_multiplicar(numero):
    numero = int(numero) #convertimos a int
    print(f"Tabla de multiplicar de {numero}:")
    for i in range(10): #repetimos 10 veces el calculo
        print(f"{numero} x {i + 1} = {numero * (i + 1)}") #multiplicamos el numero de 1..10

def operaciones_basicas(n1, n2):
    n1 = float(n1) #convertimos a float
    n2 = float(n2) #convertimos a float

    #realizamos las operaciones
    suma = n1 + n2 
    multiplicacion = n1 * n2
    division = n1 / n2
    resta = n1 - n2
    return(suma, resta, multiplicacion, division)

def calcular_imc(peso, altura):
    altura = float(altura) #convertimos a float
    peso = float(peso) #convertimos a float
    imc = (peso / ((altura) ** 2)) #calculamos el IMC con IMC = (Peso en kg) / ((Altura en metros) a la potencia 2)
    return(f"IMC del usuario: {imc:.2f}") 

def celsius_a_fahrenheit(celsius):
    celsius = int(celsius) #convertimos a int
    fahrenheit = ((celsius * (9/5)) + 32) # calculamos la conversion con Fahrenheit = (C° X (9/5)) + 32
    return(fahrenheit)

def calcular_promedio(n1, n2, n3):
    n1 = float(n1) #convertimos a float
    n2 = float(n2) #convertimos a float
    n3 = float(n3) #convertimos a float

    prom = ((n1 + n2 + n3) / 3) #sumamos los numeros y dividimos por la cantidad que hay
    return(prom)

print("funcion N° 1")
imprimir_hola_mundo()

print("funcion N° 2")
nombre = input("Nombre del saludo: ")
print(saludar_usuario(nombre))

print("funcion N° 3")
print("ingrese su informacion personal.")
nombre = input("Nombre: ")
apellido = input("apellido: ")
edad = input("edad: ")

residencia = input("residencia: ")
informacion_personal(nombre, apellido, edad, residencia)

print("funcion N° 4")
radio = input("Radio del circulo: ")
print(calcular_area_circulo(radio))
print(calcular_perimetro_circulo(radio))

print("funcion N° 5")
segundos = input("Segundos a convertir: ")
print(segundos_a_horas(segundos))

print("funcion N° 6")
numero = input("Numero para la tabla: ")
tabla_multiplicar(numero)

print("funcion N° 7")
a = input("Numero 1: ")
b = input("Numero 2: ")

suma, resta, multiplicacion, division = operaciones_basicas(a, b)
print(f"Suma: {suma}")
print(f"Resta: {resta}")
print(f"Multiplicacion: {multiplicacion}")
print(f"Division: {division:.2f}")

print("funcion N° 8")
peso = input("Peso en Kg: ")
altura = input("Altura en Metros: ")
print(calcular_imc(peso, altura))

print("funcion N° 9")
celsius = input("Grados en celsius: ")
print(f"Grados en °F {celsius_a_fahrenheit(celsius)}")

print("funcion N° 10")
a = input("Numero 1: ")
b = input("Numero 2: ")
c = input("Numero 3: ")
print(f"Promedio: {calcular_promedio(a, b, c):.2f}")