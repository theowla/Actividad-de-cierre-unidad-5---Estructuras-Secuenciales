def detectar_variables(texto): #determinamos cuales son las variables

    variables = [] #creamos la lista variables

    for item in texto: #por cada variable verificamos si ya esta guardada
        if item.isalpha() and item not in variables:
            variables.append(item)

    return variables #devolvemos variables

def generar_combinaciones(variables, actual=None, contexto_completo=None):
    #inicializamos las listas si no aparecen como argumento
    if actual is None: actual = []
    if contexto_completo is None: contexto_completo = []

    #si ya tenemos un valor para cada variable, guardamos la combinacion
    if len(actual) == len(variables):
        contexto = {}
        #unimos cada variable con su valor correspondiente
        for i in range(len(variables)):
            contexto[variables[i]] = actual[i]
        contexto_completo.append(contexto)
        return contexto_completo
    
    #primero agregamos false, y luego true recursivamente
    generar_combinaciones(variables, actual + [False], contexto_completo)
    generar_combinaciones(variables, actual + [True], contexto_completo)
    return contexto_completo

def resolver(texto, contexto):
    #traducimos los operadores logicos a python
    texto = texto.replace("∨", " or ")
    texto = texto.replace("∧", " and ")
    texto = texto.replace("⇒", " <= ")
    texto = texto.replace("→", " <= ")
    texto = texto.replace("↔", " == ")
    texto = texto.replace("⇔", " == ")
    texto = texto.replace("¬", " (not ") #abrimos un parentesis para la negacion
    texto = texto.replace("  ", " ")

    # Cerramos el paréntesis después de cada variable negada
    caracteres = []
    i = 0
    while i < len(texto):
        caracteres.append(texto[i])
        #detectamos el inicio de una negacion
        if texto[i:i+5] == "(not " and i + 5 < len(texto):
            i += 5 #saltamos al final de la negacion sumando los caracteres de not( y la variable
            #copiamos la variable negada caracter por caracter
            while i < len(texto) and texto[i].isalnum():
                caracteres.append(texto[i])
                i += 1
            #cerramos el parentesis
            caracteres.append(")")
            continue
        i += 1
    texto = "".join(caracteres)

    #ejecutamos la expresion para cada combinacion de valores
    codigo = "resultado = " + texto
    resultado = []
    for item in contexto:
        exec(codigo, {}, item)
        resultado.append(item["resultado"])
    return resultado

def corto(texto): #separamos las subproposiciones     
    resultados = []
    
    #sacamos los parentesis externos ej: (p ∧ q) = p ∧ q
    txt = texto.strip()
    if txt.startswith("(") and txt.endswith(")"):
        txt = txt[1:-1].strip()

    # buscamos subproposiciones entre paréntesis
    i = 0
    while i < len(txt):
        if txt[i] == "(":
            profundidad = 0 #cantidad de () a los que entro
            inicio = i
            for j in range(i, len(txt)):
                if txt[j] == "(": profundidad += 1 #entra en un parentesis
                elif txt[j] == ")": profundidad -= 1 #sale de un parentesis
                #cuando profundidad vuelve a 0, encontramos el cierre
                if profundidad == 0:
                    sub = txt[inicio:j+1].strip()
                    if sub not in resultados:
                        resultados.append(sub)
                    i = j
                    break
        i += 1

    #buscamos negaciones simples
    tokens = txt.split()
    for i, token in enumerate(tokens):
        if token == "¬" and i + 1 < len(tokens):
            sub = "¬" + tokens[i+1]
            if sub not in resultados:
                resultados.append(sub)

    return resultados
def tabla_verdad(texto, contexto, variables): #generamos la tabla de verdad

    tabla = {}
    dicc = {}

    # creamos las claves
    for clave in variables:
        dicc[clave] = []

    # llenamos los valores
    for diccionario in contexto:

        for clave in diccionario:

            dicc[clave].append(diccionario[clave])

    tabla.update(dicc) #lo sumamos al diccionario de la tabla
    resultados = (corto(texto)) #guardamos los resultados de corto

    for i in range(len(resultados)): #recorremos la lista
        a = resultados[i] #guardamos en una variable temporal uno de los resultados
        b = resolver(a, contexto) #lo resolvemos y lo guardamos en una variable temporal
        tabla[a] = b #lo sumamos a tabla por nombre

    tabla[texto] = resolver(texto, contexto) #guardamos el resultado de la proposicion compuesta en la tabla y sus valores

    for encabezado in tabla:
        print(encabezado, end="\t") #imprimimos los encabezados

    print()

    # filas
    filas = len(tabla[texto]) #llenamos las filas con los valores

    for i in range(filas): #imprimimos las filas

        for encabezado in tabla:

            print(tabla[encabezado][i], end="\t")

        print()

def clasificar(resultado): #clasificamos el resultado 

    if False in resultado: #comprobamos que contenga al menos 1 valor falso
        if True not in resultado: #en caso de no contener valores verdaderos
            print(">>Contradiccion") #imprimimos contradiccion
        else:
            print(">>Contingencia") #en el caso de que si contenga al menos 1 imprimimos contingencia
    else:
        print(">>Tautologia") # en caso de que no contenga al menos 1 valor falso imprimimos tautologia
    return

texto = input("Proposicion a calcular: ") #pedimos al usuario la proposicion compuesta

variables = detectar_variables(texto) #determinamos cuales son las variables
contexto = generar_combinaciones(variables) #generamos los valores para calcular las variables
tabla_verdad(texto, contexto, variables) # generamos la tabla de verdad

resultado = resolver(texto, contexto) #guardamos el valor del resultado de la proposicion
clasificar(resultado) #clasificamos la tabla
