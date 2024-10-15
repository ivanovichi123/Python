REFRESCO_PRECIO = 20
#Variable constante.
DORITOS_PRECIO = 23
#Variable constante.
PALETA_PAYASO_PRECIO = 10
#Variable constante.
costo_refresco_total = 0
#Variable que cambia en base a cuánto producto se compra.
costo_doritos_total = 0
#Variable que cambia en base a cuánto producto se compra.
costo_paleta_total = 0
#Variable que cambia en base a cuánto producto se compra.
costo_agua_total = 0
#Variable que cambia en base a cuánto producto se compra.
costo_cacahuate_total = 0
#Variable que cambia en base a cuánto producto se compra.
cantidad_total = 0
#Variable que cambia en base a cuánto producto se compra.
costo_total = 0
#Variable que cambia en base a cuánto producto se compra.
presupuesto_numero = 0
#Variable que recibirá el presupuesto del comprador.
a = 0
#variable que controla el ciclo while del presupuesto.
i = 0
#variable que controla el ciclo while de las compras.
lista = [0,0,0,0,0]
#Lista que guardará los artículos comprados en total.
cacahuate_precio = [
    [48, 48, 46, 48],
    [50, 51, 46, 35],
    [35, 30, 31, 30],
    [48, 51, 36, 34],
    [31, 46, 46, 42],
    [51, 33, 32, 42],
    [39, 50, 46, 46],
    [33, 35, 41, 45],
    [48, 33, 41, 70],
    [42, 49, 39, 35],
    [42, 30, 31, 34],
    [45, 35, 45, 33],
]
#Matriz del precio cambiante de los cacahuates según su mes y semana.

agua_precio = [
    [36, 24, 21, 20],
    [14, 13, 15, 36],
    [16, 24, 20, 13],
    [33, 33, 30, 13],
    [11, 25, 35, 23],
    [29, 15, 41, 27],
    [34, 16, 29, 29],
    [16, 33, 15, 33],
    [34, 25, 21, 13],
    [41, 40, 38, 32],
    [16, 29, 38, 16],
    [40, 13, 28, 18],
]
#Matriz del precio cambiante de la botella de agua según su mes y semana.

def recibo(presupuesto_numero):
    #Función que imprimirá todo lo necesario para un
    #recibo recibiendo el presupuesto.
    print ("Recibo:")                           
    print ("Productos comprados: ", cantidad_total)
    print ("Refrescos comprados: ",lista[0],"/",
           "Costo neto:", costo_refresco_total)
    print ("Doritos comprados: ",lista[1],"/",
           "Costo neto:", costo_doritos_total)
    print ("Paletas payaso comprados: ",lista[2],"/",
           "Costo neto:", costo_paleta_total)
    print ("Botellas de agua comprados: ",lista[3],"/",
           "Costo neto:", costo_agua_total)
    print ("Cacahuates premium comprados: ",lista[4],"/",
           "Costo neto:", costo_cacahuate_total)
    print ("Presupuesto: ", presupuesto_numero)
    print ("Costo total: ", costo_total)
    print ("Cambio: ", presupuesto_numero - costo_total)
    
def es_numero(presupuesto):
    #Función que verifica si se ingresó un número para el presupuesto.
    if presupuesto.isnumeric():
        #Si el presupuesto es un número, se sigue con la compra.
        global a
        #Utiliza la varibale global "a", en vez de utilizar una local.
        a = 1
        #Cambia la variable global "a" para detener
        #el ciclo while del presupuesto.
        global presupuesto_numero
        #Utiliza la variable global "presupuesto_numero",
        #en vez de utilizar una local.
        presupuesto_numero = int(presupuesto)
        #Convierte la string recibida a un número.
        return presupuesto_numero
        #Regresa el presupuesto.
    else:
    #Si el presupuesto no es un número se repite el ciclo
    #while hasta que reciba un número.
        print ("Ingresa un numero valido")
        return a

    
def determina_cacahuate_agua_precio(mes,semana):
    #Función que determina cuál será el precio del cacahuate y del agua.
    mes_lugar = mes - 1
    #Se resta para empezar desde el índice 0.
    semana_lugar = semana - 1
    #Se resta para empezar desde el índice 0.
    precio_cacahuate = cacahuate_precio[mes_lugar][semana_lugar]
    #Se obtiene el precio en base a los índices.
    precio_agua = agua_precio[mes_lugar][semana_lugar]
    #Se obtiene el precio en base a los índices.
    return precio_cacahuate, precio_agua
    #Regresa el precio.


mes = int(input("Selecciona el mes: "))
#Solicita el mes de la compra.
semana = int(input("Selecciona la semana: "))
#Solicita la semana de la compra.
cacahuates_premium_precio = determina_cacahuate_agua_precio(mes,semana)[0]
#Guarda en una variable el resultado de la
#función determina_cacahuate_precio.
botella_agua_precio = determina_cacahuate_agua_precio(mes,semana)[1]
#Guarda en una variable el resultado de la
#función determina_agua_precio.

while a == 0:
    #Ciclo "while", que se repite si no se da un valor
    #numérico como presupuesto.
    presupuesto = input ("¿Cual es su presupuesto?: ")
    #Pide el presupuesto de la persona.
    print ("Tu presupuesto es de: ",es_numero(presupuesto))
    #Imprime el resultado de la función "es_numero".


while i == 0:
    #Inicio del ciclo while.
    print ("[1]Refresco coca cola ($20)")
    print ("[2]Doritos ($23)")
    print ("[3]Paleta payaso ($10)")
    print (f"[4]Botella de agua (${botella_agua_precio})")
    print (f"[5]Cacahuates premium (${cacahuates_premium_precio})")
    #Los distintos productos que se pueden escoger.
    seleccion = input("Selecciona el numero del articulo que vas a comprar: ")
    if seleccion == "1":
        #Un if para saber qué producto se va a comprar.
        cantidad = int(input("Cuantos vas a comprar: "))
        #Se solicita el número de productos que se van a comprar.
        lista[0] = lista[0] + cantidad
        costo_refresco = cantidad * REFRESCO_PRECIO
        #Operación que obtiene el costo del producto en
        #base a la cantidad y el precio unitario.
        print ("Costo", costo_refresco) 
        seguir = input ("Seguir comprando [y/n]")
        if seguir == "n":
            #If para saber si se quiere seguir comprando o no.
            costo_refresco_total += costo_refresco
            #Variable que con una suma va a ir acumulando el
            #costo de todos los productos adquiridos.
            cantidad_total += cantidad
            #Variable que con una suma va a ir acumulando
            #la cantidad de prodcutos adquiridos.
            costo_total += costo_refresco
            #Variable que con una suma va a ir acumulando
            #la cantidad del costo total.
            i += 1
            #En caso de no querer seguir comprando se
            #detiene el ciclo while sumándole una unidad a "i".
            recibo (presupuesto_numero)
            #Se activa la función que creará el recibo de la compra.
        elif seguir == "y":
            #En caso de seguir comprando, el if seguirá este algoritmo.
            cantidad_total += cantidad
            #Variable que con una suma va a ir acumulando
            #la cantidad de prodcutos adquiridos.
            costo_refresco_total += costo_refresco
            #Variable que con una suma va a ir acumulando
            #el costo de todos los productos adquiridos.
            costo_total += costo_refresco
            #Variable que con una suma va a ir acumulando
            #la cantidad del costo total.
            i = i
            #Al querer seguir comprando se repetirá el ciclo while.
    elif seleccion == "2":
        #Un if para saber qué producto se va a comprar.
        cantidad = int(input ("Cuantos vas a comprar: "))
        #Se solicita el número de productos que se van a comprar.          
        lista[1] = lista[1] + cantidad
        costo_doritos = cantidad * DORITOS_PRECIO
        #Operación que obtiene el costo del producto en
        #base a la cantidad y el precio unitario.
        print ("Costo", costo_doritos)      
        seguir = input ("Seguir comprando [y/n]")       
        if seguir == "n":
            #If para saber si se quiere seguir comprando o no.
            costo_doritos_total += costo_doritos
            #Variable que con una suma va a ir acumulando
            #el costo de todos los productos adquiridos.
            cantidad_total += cantidad
            #Variable que con una suma va a ir acumulando
            #la cantidad de prodcutos adquiridos.
            costo_total += costo_doritos
            #Variable que con una suma va a ir acumulando
            #la cantidad del costo total.
            i += 1
            #En caso de no querer seguir comprando se
            #detiene el ciclo while sumándole una unidad a "i".
            recibo (presupuesto_numero)
            #Se activa la función que creará el recibo de la compra.
        elif seguir == "y":
            #En caso de seguir comprando, el if seguirá este algoritmo.
            costo_doritos_total += costo_doritos
            #Variable que con una suma va a ir acumulando
            #el costo de todos los productos adquiridos.
            cantidad_total += cantidad
            #Variable que con una suma va a ir acumulando
            #la cantidad de prodcutos adquiridos.
            costo_total += costo_doritos
            #Variable que con una suma va a ir acumulando
            #la cantidad del costo total.
            i = i
            #Al querer seguir comprando se repetirá el ciclo while.
    elif seleccion == "3":
        #Un if para saber qué producto se va a comprar.
        cantidad = int(input("Cuantos vas a comprar: "))
        #Se solicita el número de productos que se van a comprar.
        lista[2] = lista[2] + cantidad
        costo_paleta = cantidad * PALETA_PAYASO_PRECIO
        #Operación que obtiene el costo del producto en
        #base a la cantidad y el precio unitario.
        print ("Costo", costo_paleta)                   
        seguir = input ("Seguir comprando [y/n]")
        if seguir == "n":
            #If para saber si se quiere seguir comprando o no.
            costo_paleta_total += costo_paleta
            #Variable que con una suma va a ir acumulando
            #el costo de todos los productos adquiridos.
            cantidad_total += cantidad
            #Variable que con una suma va a ir acumulando
            #la cantidad de prodcutos adquiridos.
            costo_total += costo_paleta
            #Variable que con una suma va a ir acumulando
            #la cantidad del costo total.
            i += 1
            #En caso de no querer seguir comprando se
            #detiene el ciclo while sumándole una unidad a "i".
            recibo (presupuesto_numero)
            #Se activa la función que creará el recibo de la compra.
        elif seguir == "y":
            #En caso de seguir comprando, el if seguirá este algoritmo.
            costo_paleta_total += costo_paleta
            #Variable que con una suma va a ir acumulando
            #el costo de todos los productos adquiridos.
            cantidad_total += cantidad
            #Variable que con una suma va a ir acumulando
            #la cantidad de prodcutos adquiridos.
            costo_total += costo_paleta
            #Variable que con una suma va a ir acumulando
            #la cantidad del costo total.
            i = i
            #Al querer seguir comprando se repetirá el ciclo while.
    elif seleccion == "4":
        #Un if para saber qué producto se va a comprar.
        cantidad = int(input("Cuantos vas a comprar: "))
        #Se solicita el número de productos que se van a comprar.
        lista[3] = lista[3] + cantidad
        costo_agua = cantidad * botella_agua_precio
        #Operación que obtiene el costo del producto en
        #base a la cantidad y el precio unitario.
        print ("Costo", costo_agua)
        seguir = input ("Seguir comprando [y/n]")
        if seguir == "n":
            #If para saber si se quiere seguir comprando o no.
            costo_agua_total += costo_agua
            #Variable que con una suma va a ir acumulando
            #el costo de todos los productos adquiridos.
            cantidad_total += cantidad
            #Variable que con una suma va a ir acumulando
            #la cantidad de prodcutos adquiridos.
            costo_total += costo_agua
            #Variable que con una suma va a ir acumulando
            #la cantidad del costo total.
            i += 1
            #En caso de no querer seguir comprando
            #se detiene el ciclo while sumándole una unidad a "i".
            recibo (presupuesto_numero)
            #Se activa la función que creará el recibo de la compra.
        elif seguir == "y":
            #En caso de seguir comprando, el if seguirá este algoritmo.
            costo_agua_total += costo_agua
            #Variable que con una suma va a ir acumulando
            #el costo de todos los productos adquiridos.
            cantidad_total += cantidad
            #Variable que con una suma va a ir acumulando
            #la cantidad de prodcutos adquiridos.
            costo_total += costo_agua
            #Variable que con una suma va a ir acumulando
            #la cantidad del costo total.
            i = i
            #Al querer seguir comprando se repetirá el ciclo while.
    elif seleccion == "5":
        #Un if para saber qué producto se va a comprar.
        cantidad = int(input("Cuantos vas a comprar: "))
        #Se solicita el número de productos que se van a comprar.
        lista[4] = lista[4] + cantidad
        costo_cacahuate = cantidad * cacahuates_premium_precio
        #Operación que obtiene el costo del producto en
        #base a la cantidad y el precio unitario.
        print ("Costo", costo_cacahuate)                
        seguir = input ("Seguir comprando [y/n]")
        if seguir == "n":
            #If para saber si se quiere seguir comprando o no.
            costo_cacahuate_total += costo_cacahuate
            #Variable que con una suma va a ir acumulando
            #el costo de todos los productos adquiridos.
            cantidad_total += cantidad
            #Variable que con una suma va a ir acumulando
            #la cantidad de prodcutos adquiridos.
            costo_total += costo_cacahuate
            #Variable que con una suma va a ir acumulando
            #la cantidad del costo total.
            i += 1
            #En caso de no querer seguir comprando se
            #detiene el ciclo while sumándole una unidad a "i".
            recibo (presupuesto_numero)
            #Se activa la función que creará el recibo de la compra.
        elif seguir == "y":
            #En caso de seguir comprando, el if seguirá este algoritmo.
            costo_cacahuate_total += costo_cacahuate
            #Variable que con una suma va a ir acumulando
            #el costo de todos los productos adquiridos.
            cantidad_total += cantidad
            #Variable que con una suma va a ir acumulando
            #la cantidad de prodcutos adquiridos.
            costo_total += costo_cacahuate
            #Variable que con una suma va a ir acumulando
            #la cantidad del costo total.
            i = i
            #Al querer seguir comprando se repetirá el ciclo while.