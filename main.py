
while True:
    nombre = input("Nombre: ")
    
    if nombre.isalpha():
        nombre = nombre.title()
        break
    else:
        print("El nombre debe no estar vacio y estar compuesto por letras")
while True:
    productos = (input("Cantidad de productos: "))

    if productos.isdigit():
        productos = int(productos)
        if productos > 0:
            break
        else:
            print("La cantidad de productos debe ser un digito entero y positivo")
    else:
        print("La cantidad de productos debe ser un digito entero y positivo")

total = 0
total_descuento = 0
resumen = ""
for i in range(productos):
    while True:
        precio = (input("precio: "))
        if precio.isdigit():
            precio = int(precio)
            if precio > 0:
                break
            else:
                print("El precio debe ser un numero positivo")
    while True:
        descuento = input("¿Tiene descuento? (S/N) ")
        if descuento == "s" or descuento == "S":
            precio_descuento = (precio * 0.90)
            total_descuento = (total_descuento + precio_descuento)
            break
        elif descuento == "n" or descuento == "N":
            total_descuento = (total_descuento + precio)
            break
        else:
            print("Descuento debe ser s/n")

    total = (total + precio)
    resumen += (f"Producto {i+1} - Precio: ${precio} Descuento (S/N): {descuento}\n\n")
ahorro = (total - total_descuento)
promedio = (total_descuento / productos)
print(f"Cliente: {nombre}")
print(resumen)
print(f"Total sin descuentos: ${total:.2f}\nTotal con descuentos: ${total_descuento:.2f}\nAhorro: ${ahorro:.2f}\nPromedio por producto: ${promedio:.2f}")

# segundo ejercicio

usuario_correcto = "alumno"
clave_correcta = "python123"
mensaje_motivacional = "gukgkg"
intentos = 0

while intentos < 3:
    usuario = input(f"Intento {intentos+1}/3 Usuario: ")
    clave = input("Clave: ")
    if usuario == usuario_correcto and clave == clave_correcta:
        print("1) Estado  2) Cambiar clave  3) Mensaje  4) Salir")
        while True:
            opcion = input("Opcion: ")
            if (opcion.isdigit()):
                opcion = int(opcion)
                if opcion > 4 or opcion < 1:
                    print("Error: opción fuera de rango.")
                elif opcion == 1:
                    print("Estado: Inscripto")                      
                elif opcion == 2:
                    while True:
                        clave_nueva = input("Clave nueva: ")
                        confirmacion = input("Confirmacion de clave:")
                        if len(clave_nueva) >= 6:
                            if clave_nueva == confirmacion:
                                clave_correcta = clave_nueva
                                break
                            else:
                                print("Error: La clave y su confirmacion deben coincidir") 
                        else:
                            print("Error: mínimo 6 caracteres.")
                elif opcion == 3:
                    print(mensaje_motivacional)
                elif opcion == 4:
                    break
            else:
                print("Error: ingrese un número válido.")
        break
    else:
        print("Error: credenciales inválidas.")
        intentos += 1
        
if intentos == 3:
    print("Cuenta bloqueada")

# ejercicio 3
lunes1 = ""
lunes2 = ""
lunes3 = ""
lunes4 = ""
martes1 = ""
martes2 = ""
martes3 = ""

cant_reservas = 0
cant_reservas2 = 0

while True:
    nombre = input("Nombre del operador")
    if nombre.isalpha():
        break
    else:
        print("El nombre solo debe contener letras")
while True:
    print("1. Reservar turno\n2. Cancelar turno (por nombre)\n3. Ver agenda del día\n4. Ver resumen general\n5. Cerrar sistema ")
    opcion = input("opcion: ")

    if opcion.isdigit():
        opcion = int(opcion)
        if opcion == 1:
            while True:
                dia_reserva = input("")
                if dia_reserva.isdigit():
                    dia_reserva = int(dia_reserva)
                    if dia_reserva >= 1 and dia_reserva <= 2:
                        break
                else:
                    print("")
            while True:
                nombre_reserva = input("")
                if nombre_reserva.isalpha():
                    break
                else:
                    print("")
            if dia_reserva == 1:
                if (nombre_reserva == lunes1 or nombre_reserva == lunes2 or nombre_reserva == lunes3 or nombre_reserva == lunes4):
                    print("ya hay reserva en ese dia")
                elif lunes1 == "":
                    lunes1 = nombre_reserva
                    cant_reservas += 1
                elif lunes2 == "":
                    lunes2 = nombre_reserva 
                    cant_reservas += 1
                elif lunes3 == "":
                    lunes3 = nombre_reserva 
                    cant_reservas += 1
                elif lunes4 == "":
                    lunes4 = nombre_reserva
                    cant_reservas += 1
                else:
                    print("No hay turnos disponibles") 
            elif dia_reserva == 2:
                if (nombre_reserva == martes1 or nombre_reserva == martes2 or nombre_reserva == martes3):
                    print("ya hay reserva en ese dia")
                elif martes1 == "":
                    martes1 = nombre_reserva
                    cant_reservas2 += 1                     
                elif martes2 == "":
                    martes2 = nombre_reserva
                    cant_reservas2 += 1
                elif martes3 == "":
                    martes3 = nombre_reserva
                    cant_reservas2 += 1
                else:
                    print("No hay turnos disponibles") 

        elif opcion == 2:
            while True:
                dia_cancelar = input("Elegir dia (1=Lunes, 2=Martes): ")
                if dia_cancelar.isdigit():
                    dia_cancelar = int(dia_cancelar)
                    if 1 <= dia_cancelar <= 2:
                        break
                    else:
                        print("La opcion de dia debe ser entre 1 o 2")
                else:
                    print("La opcion de dia debe ser hecha con numeros")
            while True:
                nombre_reserva = input("Nombre de la reserva: ")
                if nombre_reserva.isalpha():
                    break
                else:
                    print("El nombre debe solo contener letras")
            if dia_cancelar == 1:
                if lunes1 == nombre_reserva:
                    lunes1 = ""
                    cant_reservas -= 1
                elif lunes2 == nombre_reserva:
                    lunes2 = ""
                    cant_reservas -= 1 
                elif lunes3 == nombre_reserva:
                    lunes3 = "" 
                    cant_reservas -= 1 
                elif lunes4 == nombre_reserva:
                    lunes4 = ""
                    cant_reservas -= 1 
                else:
                    print("No hay turnos con ese nombre reservados") 
            elif dia_cancelar == 2:
                if martes1 == nombre_reserva:
                    martes1 = ""  
                    cant_reservas2 -= 1                    
                elif martes2 == nombre_reserva:
                    martes2 = ""
                    cant_reservas2 -= 1
                elif martes3 == nombre_reserva:
                    martes3 = ""
                    cant_reservas2 -= 1
                else:
                    print("No hay turnos con ese nombre reservados") 
        elif opcion == 3:
            while True:
                dia_reserva = input("Elegir dia (1=Lunes, 2=Martes): ")
                if dia_reserva.isdigit():
                    dia_reserva = int(dia_reserva)
                    if 1 <= dia_reserva <= 2:
                        break
                    else:
                        print("Dia invalido")
                else:
                    print("Ingrese un numero valido")
            if dia_reserva == 1:
                print("Agenda Lunes:")
                print(f"Turno 1: {lunes1 if lunes1 != '' else '(libre)'}")
                print(f"Turno 2: {lunes2 if lunes2 != '' else '(libre)'}")
                print(f"Turno 3: {lunes3 if lunes3 != '' else '(libre)'}")
                print(f"Turno 4: {lunes4 if lunes4 != '' else '(libre)'}")
            elif dia_reserva == 2:
                print("Agenda Martes:")
                print(f"Turno 1: {martes1 if martes1 != '' else '(libre)'}")
                print(f"Turno 2: {martes2 if martes2 != '' else '(libre)'}")
                print(f"Turno 3: {martes3 if martes3 != '' else '(libre)'}")

        elif opcion == 4:
            print(f"turnos disponibles Martes: {3 - cant_reservas2}")
            print(f"turnos ocupados Martes: {cant_reservas2}")
            print(f"turnos disponibles Lunes: {4 - cant_reservas}")
            print(f"turnos ocupados Lunes: {cant_reservas}")
            if cant_reservas > cant_reservas2:
                print("El dia lunes tiene mas turnos")
            elif cant_reservas2 > cant_reservas:
                print("El dia martes tiene mas turnos")
            else:
                print("Ambos dias tienes la misma cantidad de turnos")
        elif opcion == 5:
            break
#ejercicio 4
energia = 100 
tiempo = 12 
cerraduras_abiertas = 0 
alarma = False 
codigo_parcial = "" 

racha_forzar = 0 

while True:
    nombre = input("Ingrese nombre del agente: ")
    if nombre.isalpha():
        break

while energia > 0 and tiempo > 0 and cerraduras_abiertas < 3:

    if alarma and tiempo <= 3 and cerraduras_abiertas < 3:
        print("Bloqueo por alarma")
        break

    print("--- ESTADO ---")
    print(f"Energía: {energia}")
    print(f"Tiempo: {tiempo}")
    print(f"Cerraduras abiertas: {cerraduras_abiertas}")
    print(f"Alarma: {alarma}")
    print(f"Código parcial: {codigo_parcial}")

    print("1. Forzar cerradura")
    print("2. Hackear panel")
    print("3. Descansar")

    while True:
        opcion = input("Elija una opcion: ")
        if opcion.isdigit() and int(opcion) in
        break
    if opcion == 1:
        energia -= 20
        tiempo -= 2
        racha_forzar += 1

        if racha_forzar == 3:
            alarma = True
            print("la cerradura se trabo")
            continue

        if energia < 40 and not alarma:
            while True:
                num = input("riesgo elija 1-3")
                if num.isdigit() and int(num) in 123:
                    num = int(num)
                    break
            if num == 3:
                alarma = True
                print("se activo la alarma")
        if not alarma:
            cerraduras_abiertas += 1
            print("abriste una cerradura")
    elif opcion == 2:
        energia -= 10
        tiempo -= 3
        racha_forzar = 0

        print("hackeando")
        for i in range(4):
            print(f"progreso {i+1}/4")
            codigo_parcial += "A"
        
        if len(codigo_parcial) >= 8 and cerraduras_abiertas < 3:
            cerraduras_abiertas += 1
            print("codigo completo se abrio la cerradura")
    elif opcion == 3:
        tiempo -=1
        racha_forzar = 0

        energia += 15
        if energia > 100:
            energia = 100
        
        if alarma:
            energia -= 10
            print("descansar coon la alarma consume energia extra")
        
        print("descansaste")
print("resultado")
if cerraduras_abiertas == 3:
    print("ganaste")
elif energia <= 0 or tiempo <= 0:
    print("derrota por energia/tiempo")
elif alarma and tiempo <= 3:
    print("derrota el sistema se bloqueo por alarma")
