precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}  

#actividad 1
precios_frutas['Naranja'] = "1200"
precios_frutas['Manzana'] = "1500"
precios_frutas['Pera'] = "2300"

print(precios_frutas)

#actividad 2
precios_frutas['Banana'] = "1330"
precios_frutas['Manzana'] = "1700"
precios_frutas['Melón'] = "2800"

print(precios_frutas)


#actividad 3
frutas = precios_frutas.keys()

print(frutas)

#actividad 4
contactos = {}

def lista_contactos():
    for i in range(5):
        n = True
        while n:
            print(f"Contacto N° {i + 1}")
            contacto = input("Contacto: ")
            numero = input("Numero: ")
            if contacto.isalpha() and numero.isdigit():
                if contacto not in contactos:
                    contactos[contacto] = numero
                    n = False
                else:
                    print("Contacto ya registrado")
            else:
                print("Contacto invalido")

def consultar(nombre):
    if nombre in contactos:
        print(contactos[nombre])
    else:
        print("Este contacto no existe")

#lista_contactos()
#consultar(input("Contacto a consultar: "))

#actividad 5

#texto = input("frase: ")

def palabras_unicas(texto):
    if texto != "":
        frase = texto.split()
        dict_frases = {}
        palabras = set(frase)

        for i in range(len(frase)):
            if frase[i] not in dict_frases:
                dict_frases[frase[i]] = 1    
            else:
                dict_frases[frase[i]] += 1 

        print(palabras)
        print(dict_frases)
    else:
        print("Texto vacio")
#palabras_unicas(texto)
#actividad 6

alumnos = {
    "Sofia": (10, 9, 8),
    "Luis": (6, 7, 7)
}

for key in alumnos:
    promedio_alumno = sum(alumnos[key])
    print(f"{key}: {(promedio_alumno / 3):.2f}")

#actividad 7
asistencias = ["Ana", "Luis", "Ana", "Maria", "Luis", "Pedro", "Ana"]
def palabras_unicas(asistencias):

    dict_asistencias = {}
    empleados = set(asistencias)

    for i in range(len(asistencias)):
        if asistencias[i] not in dict_asistencias:
            dict_asistencias[asistencias[i]] = 1    
        else:
            dict_asistencias[asistencias[i]] += 1 

    print(asistencias)
    print(empleados)
    print(dict_asistencias)

#palabras_unicas(asistencias)
#ejercicio 8
def a():
    productos = {}

    producto = input("producto: ")

    if producto in productos:
        print("a")  
    else:
        print("consultar stock: 1")
        print("agregar unidades al stock: 2")
        print("agregar producto: 3")

    opcion = input("Opcion: ")
    opcion = int(opcion)
    if opcion == 1:
        productos[producto]
    elif opcion == 2:
        cantidad = input("Cantidad a agregar a stock: ")
        if cantidad.isdigit() and cantidad > 0:
            productos[producto] += cantidad
        else:
            print("cantidad invalida")
    elif opcion == 3:
        productos[producto] = 0
    else:
        print("opcion invalida")

#actividad 9
def agenda():
    agenda = {
        ("lunes", "10:00"): "Reunión",
        ("martes", "15:00"): "Clase de inglés"
    }

    consulta_dia = input("Dia: ").lower()
    consulta_hora = input("Horario: ")
    consulta = (consulta_dia, consulta_hora)
    if consulta_hora and consulta_dia:
        if consulta in agenda:
            print(agenda[consulta_dia, consulta_hora])
        else:
            print("No existe nada en agenda para esa fecha.")
    else:
        print("Fecha/Dia invalido.")
agenda()
#actividad 10

original = {"Argentina": "Buenos Aires", "Chile": "Santiago"}
invertido = {}

for key in original:
    value = original[key]
    invertido[value] = key

print(original)
print(invertido)