# para ejecutar cada funcion se debe usar "python main.py NombreDeLaFuncion" en la terminal

def helloWorld():
    print("hola mundo")

def helloName():
    name = input("nombre: ")
    print(f"Hola {name}!")

def Person():
    name = input("nombre: ")
    lastName = input("apellido: ")
    age = input("edad:")
    country = input("pais: ")
    print(f"Soy {name} {lastName} tengo {age} años y vivo en {country}")

def circle():
    radius = input("radio del circulo: ") 
    radius = float(radius)
    perimeter = ((2 * 3.14) * radius)
    area = (3.14 * (radius ** 2))
    print(f"area: {area}, perimetro: {perimeter}")

def secondsToHours():
    seconds = input("segundos:")
    seconds = int(seconds)
    hours = (seconds / 3600)
    hours = int(hours)
    print(hours)

def timesTables():
    n = input("numero: ")
    n = int(n)
    for i in range(11):
        table = n * i
        print(table)

def calculate():
    n1 = input("n1: ")
    n2 = input("n2: ")
    n1 = int(n1)
    n2 = int(n2)

    add = n1 + n2
    multip = n1 * n2
    div = n1 / n2
    subt = n1 - n2
    print(f"suma: {add}, resta: {subt}, multiplicacion: {multip}, division: {div}")

def bmi():
    height = int(input("altura: "))
    weight = int(input("peso en kg: "))
    imc = (weight / ((height / 100) ** 2))
    print(imc)

def csToFh():
    temp = int(input("grados celsius: "))
    fahrenheit = ((temp * (9/5)) + 32)
    print(fahrenheit)

def average():
    n1 = int(input("n1: "))
    n2 = int(input("n2: "))
    n3 = int(input("n3: "))

    prom = ((n1 + n2 + n3) / 3)
    print(prom)


functions = {
    "helloWorld" : helloWorld,
    "helloName" : helloName,
    "Person" : Person,
    "circle" : circle,
    "secondsToHours" : secondsToHours,
    "timesTables" : timesTables,
    "calculate" : calculate,
    "bmi" : bmi,
    "csToFh" : csToFh,
    "average" : average,
}

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1:
        func_name = sys.argv[1]
        fn = functions.get(func_name)
        if fn:
            fn()
        else:
            print("funcion no encontrada")