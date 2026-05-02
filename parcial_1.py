
#inicializamos las listas
herramientas = []
existencias = []

while True:
    opcion = input("opción: ") #pedimos la opcion al usuario
    if opcion.isdigit(): #validamos la opcion
        opcion = int(opcion) #convertimos a integer
        
        if opcion == 1: #opcion 1 carga de herramientas a la lista
            print(">> Carga Inicial de Herramientas.")

            while True:
                n = input("Cantidad de herramientas: ") #pedimos la cantidad de herramientas que habrá
                if n.isdigit() and int(n) > 0: #validamos el numero
                    n = int(n) #convertimos a integer
                    break
                else:
                    print("Error: Cantidad inválida.")

            #por cada herramienta pedimos su nombre
            for i in range(n):
                while True:
                    nombre = input(f"Nombre de la herramienta {i + 1}/{n}: ") #pedimos el nombre

                    if nombre.isalpha(): #validamos el nombre
                        nombre = nombre.lower() #estandarizamos la variable

                        if nombre not in herramientas: #si no está dentro de herramientas la agregamos (para no repetir herramientas)
                            herramientas.append(nombre) 
                            break
                        else: #si esta repetida devolvemos error
                            print(f"Error: {nombre} ya está en la lista.")
                    else:
                        print("Error: herramienta inválida.")

        elif opcion == 2: # opcion 2 carga de existencias
            print(">> Carga de Existencias.")

            if len(herramientas) > 0: #verificamos que haya herramientas en la lista para sumar sus existencias
                existencias = [] #reiniciamos la lista para evitar repeticiones
                for i in range(len(herramientas)): #por cada herramienta pedimos su stock
                    while True:
                        cantidad = input(f"Existencias de {herramientas[i]}: ") # pedimos stock

                        if cantidad.isdigit() and int(cantidad) >= 0: #validamos la cantidad y evitamos numeros menores a 0
                            cantidad = int(cantidad) # convertimos a integer
                            existencias.append(cantidad) # sumamos las existencias a la lista
                            print(f"{herramientas[i]}: {existencias[i]}.") # imprimimos la herramienta y sus existencias
                            break
                        else:
                            print("Error: Cantidad inválida.")
            else:
                print("Error: primero debe cargar herramientas.")

        elif opcion == 3: #opcion 3 mostrar stock
            print(">> Visualización de Inventario.")

            if len(herramientas) > 0 and len(herramientas) == len(existencias): # verificamos que haya herramientas y tenga sus respectivas existencias
                for i in range(len(herramientas)): #imprimimos todo el stock item por item
                    print(f"{herramientas[i]}: {existencias[i]} unidades.") 
            else:
                print("Error: primero debe cargar herramientas y existencias.")

        elif opcion == 4: # opcion 4 buscar en stock
            print(">> Consulta de Stock (existencias).")

            if len(herramientas) > 0 and len(herramientas) == len(existencias): # verificamos que haya herramientas y tenga sus respectivas existencias

                while True:
                    nombre = input("Nombre de la herramienta: ") #pedimos el nombre de la herramienta a consultar
                    if nombre.isalpha(): # validamos el formato
                        nombre = nombre.lower() # estandarizamos los nombres

                        if nombre in herramientas: # verificamos que este en stock la herramienta
                            stock = herramientas.index(nombre) # buscamos donde se ubica en la lista
                            print(f"Stock de {nombre}: {existencias[stock]}.") # imprimimos la herramienta y la existencia ayudandonos del index de la misma
                            break
                        else:
                            print("Error: No está en el listado.")
                    else:
                        print("Error: nombre invalido.")
            else:
                print("Error: primero debe cargar herramientas y existencias.")

        elif opcion == 5: # opcion 5 lista de agotados
            print(">> Reporte de Agotados.")

            if len(herramientas) > 0 and len(herramientas) == len(existencias): # verificamos que haya herramientas y tenga sus respectivas existencias
                print("Listado de agotados: ") 
                for i in range(len(herramientas)): # por cada herramienta buscamos su stock y verificamos que sea 0
                    if existencias[i] == 0: # en caso de ser 0 la imprimimos junto a la lista
                        print(f"{herramientas[i]}: Agotado.")
            else:
                print("Error: primero debe cargar herramientas y existencias.")
        elif opcion == 6: # opcion 6 agregar una herramienta nueva
            print(">> Alta de Nuevo Producto.")

            #pedimos nombre y las existencias de la herramienta
            nombre = input("Nombre de la herramienta nueva: ")
            cantidad = input("Cantidad: ")

            if nombre.isalpha() and cantidad.isdigit() and int(cantidad) >= 0: #validamos los inputs
                nombre = nombre.lower() #estandarizamos el nombre
                cantidad = int(cantidad) #convertimos a integer la cantidad

                if nombre not in herramientas: # si no esta en herramientas
                    herramientas.append(nombre) # sumamos el nombre a la lista
                    existencias.append(cantidad) # sumamos las existencias 
                    print(f"{nombre} fue agregado a la lista.") # devolvemos una confirmación
                else:
                    print(f"Error: {nombre} ya esta en la lista.") # en caso de error terminamos el proceso como lo pide la actividad
            else:
                print("Error: valores inválidos.") # en caso de error terminamos el proceso como pide la actividad
        elif opcion == 7: # opcion 7 vender o agregar herramientas
            print(">> Actualización de Stock (Venta/Ingreso).")
            
            if len(herramientas) > 0 and len(herramientas) == len(existencias): # comentario

                while True:
                    accion = input("Venta o ingreso: ") # pedimos la acción a realizar

                    if accion.isalpha(): # validamos el formato de la accion
                        accion = accion.lower() # estandarizamos la accion
                        if accion == "venta" or accion == "ingreso": # verificamos que la acción sea correctamente escrita
                            break
                        else:
                            print("Error: opción inválida.")
                    else:
                        print("Error: valor inválido.")
                while True:
                    nombre = input("Nombre de la herramienta: ") # pedimos el nombre de la herramienta sobre la cual realizar al accion
                    cantidad = input("Cantidad: ") # pedimos la cantidad

                    if nombre.isalpha() and cantidad.isdigit() and int(cantidad) > 0: # validamos cantidad y el formato del nombre
                        cantidad = int(cantidad) # convertimos a integer
                        if nombre in herramientas: # verificamos que exista en la lista
                            index = herramientas.index(nombre) # buscamos su index

                            if accion == "venta": #en el caso de venta
                                if cantidad <= existencias[index]: # verificamos que hayan suficientes existencias para vender
                                    existencias[index] -= cantidad # restamos de las existencias lo vendido
                                    break
                                else:
                                    print("Error: sin existencias suficientes.")
                                    break

                            elif accion == "ingreso" and int(cantidad) > 0: # en el caso de ingreso de existencias
                                existencias[index] += cantidad # sumamos la cantidad al stock
                                break
                        else:
                            print("Error: esta herramienta no existe en la lista.")
                            break
                    elif nombre.isalpha() and (not cantidad.isdigit() or int(cantidad) <= 0):
                        print("Error: cantidad inválida.")
                    else:
                        print("Error: nombre inválido.")
            else:
                print("Error: primero debe cargar herramientas y existencias.")

        elif opcion == 8: # opcion 8 salir del programa
            print("Saliendo del programa.") # imprimimos un mensaje y cerramos el loop while
            break
        else:
            print("Error opción fuera de rango")
    else: #en el caso de que esté vacía o fuera de rango la opcion devolvemos error
        print("Error: opción inválida.")
