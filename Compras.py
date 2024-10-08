REFRESCO_PRECIO = 20            #variable constante
DORITOS_PRECIO = 23             #variable constante
PALETA_PAYASO_PRECIO = 10       #variable constante
BOTELLA_AGUA_PRECIO = 13        #variable constante
CACAHUATES_PREMIUM_PRECIO = 30  #variable constante
costo_refresco_total = 0        #variable que cambia en base a cuanto producto se compra
costo_doritos_total = 0         #variable que cambia en base a cuanto producto se compra
costo_paleta_total = 0          #variable que cambia en base a cuanto producto se compra
costo_agua_total = 0            #variable que cambia en base a cuanto producto se compra
costo_cacahuate_total = 0       #variable que cambia en base a cuanto producto se compra
cantidad_numero_total = 0       #variable que cambia en base a cuanto producto se compra
costo_total = 0					#variable que cambia en base a cuanto producto se compra
presupuesto_numero = 0          #Variable que recibira el presupuesto del comprador
a = 0                           #variable que controla el ciclo while del presupuesto
i = 0                           #variable que controla el ciclo while de las compras
lista = [0,0,0,0,0]				#Lista que guardara los articulos comprados en total
cacahuate_precio = [			#Matriz del precio cambiante de los cacahuates segun su mes y semana
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

botella_agua_precio = [			#Matriz del precio cambiante de la botella de agua segun su mes y semana
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

def recibo(presupuesto_numero):                 #Funcion que imprimira todo lo necesario para un recibo recibiendo el presupuesto
    print ("Recibo:")                           
    print ("Productos comprados: ", cantidad_numero_total)
    print ("Refrescos comprados: ",lista[0],"/","Costo neto:", costo_refresco_total)
    print ("Doritos comprados: ",lista[1],"/","Costo neto:", costo_doritos_total)
    print ("Paletas payaso comprados: ",lista[2],"/","Costo neto:", costo_paleta_total)
    print ("Botellas de agua comprados: ",lista[3],"/","Costo neto:", costo_agua_total)
    print ("Cacahuates premium comprados: ",lista[4],"/","Costo neto:", costo_cacahuate_total)
    print ("Presupuesto: ", presupuesto_numero)
    print ("Costo total: ", costo_total)
    cambio = presupuesto_numero - costo_total   #Operacion que calcula el cambio en base al presupuesto y el costo total
    print ("Cambio: ", cambio)
    
def es_numero(presupuesto):                         #Funcion que verifica si se ingreso un numero para el presupuesto
    if presupuesto.isnumeric():                     #Si el presupuesto es un numero, se sigue con la compra
        global a                                    #Utiliza la varibale global "a", en vez de utilizar una local
        a = 1                                       #Cambia la variable global "a" para detener el ciclo while del presupuesto
        global presupuesto_numero                   #Utiliza la variable global "presupuesto_numero", en vez de utilizar una local
        presupuesto_numero = int(presupuesto)       #Convierte la string recibida a un numero
        return presupuesto_numero                   #Regresa el presupuesto
    else:                                           #Si el presupuesto no es un numero se se repite el ciclo while hasta que reciba un numero
        a = 0
        print ("Ingresa un numero valido")
        return a                                    #Regresa "a" y se repetira el ciclo del presupuesto
    
def determina_cacahuate_precio(mes,semana):				#Funcion que determina cual sera el precio del cacahuate
    mes_lugar = mes - 1									#Se resta para emepzar desde el indice 0
    semana_lugar = semana - 1							#Se resta para empezar desde el indice 0
    precio = cacahuate_precio[mes_lugar][semana_lugar]	#Se obtiene el precio en base a los indices
    return precio										#Regresa el precio

def determina_agua_precio(mes,semana):				#Funcion que determina cual sera el precio del agua
    mes_lugar = mes - 1									#Se resta para emepzar desde el indice 0
    semana_lugar = semana - 1							#Se resta para empezar desde el indice 0
    precio = botella_agua_precio[mes_lugar][semana_lugar]	#Se obtiene el precio en base a los indices
    return precio	
        
mes = int(input("Selecciona el mes: "))					#Solicita el mes de la compra
semana = int(input("Selecciona la semana: "))			#Solicita la semana de la compra
cacahuates_premium_precio = determina_cacahuate_precio(mes,semana)	#Guarda en una variable el resultado de la funcion determina_cacahuate_precio
botella_agua_precio_determinado = determina_agua_precio(mes,semana)				#Guarda en una variable el resultado de la funcion determina_agua_precio	


while a == 0:                                               #ciclo "while", que se repite si no se da un valor numerico como presupuesto
    presupuesto = input ("¿Cual es su presupuesto?: ")      #Pide el presupuesto de la persona
    print ("Tu presupuesto es de: ",es_numero(presupuesto)) #Imprime el resultado de la funcion "es_numero"


while i == 0:                                       #Incio del ciclo while
    print ("[1]Refresco coca cola ($20)")           #Los distintos productos que se pueden escoger
    print ("[2]Doritos ($23)")
    print ("[3]Paleta payaso ($10)")
    print (f"[4]Botella de agua (${botella_agua_precio_determinado})")
    print (f"[5]Cacahuates premium (${cacahuates_premium_precio})")
    seleccion = input("Selecciona el numero del articulo que vas a comprar: ")
    if seleccion == "1":                                #Un if para saber que producto se va a comprar
        cantidad = input("Cuantos vas a comprar: ")     #Se solicita el numero de productos que se van a comprar
        cantidad_numero = int(cantidad)                 #Convierte la string recibida a un numero entero
        cantidad_total_refresco = lista[0] + cantidad_numero	#
        lista[0] = cantidad_total_refresco
        costo_refresco = cantidad_numero * REFRESCO_PRECIO      #Operacion que obtiene el costo del producto en base a la cantidad y el precio unitario
        print ("Costo", costo_refresco)
        seguir = input ("Seguir comprando [y/n]")
        if seguir == "n":                               #If para saber si se quiere seguir comprando o no
            costo_refresco_total += costo_refresco      #Variable que con una suma va a ir acumulando el costo de todos los productos adquiridos
            cantidad_numero_total += cantidad_numero    #Variable que con una suma va a ir acumulando la cantidad de prodcutos adquiridos
            costo_total += costo_refresco_total         #Variable que con una suma va a ir acumulando la cantidad del costo total 
            i = i + 1                                   #En caso de no querer seguir comprando se detiene el cilco while sumandole una unidad a "i"
            recibo (presupuesto_numero)                 #Se activa la funcion que creara el recibo de la compra
        elif seguir == "y":                             #En caso de seguir comprando el if seguira este algoritmo
            cantidad_numero_total += cantidad_numero    #Variable que con una suma va a ir acumulando la cantidad de prodcutos adquiridos
            costo_refresco_total += costo_refresco      #Variable que con una suma va a ir acumulando el costo de todos los productos adquiridos
            costo_total += costo_refresco_total         #Variable que con una suma va a ir acumulando la cantidad del costo total
            i = i                                       #Al querer seguir comprando se repetira el ciclo while
    elif seleccion == "2":                              #Un if para saber que producto se va a comprar
        cantidad = input ("Cuantos vas a comprar: ")    #Se solicita el numero de productos que se van a comprar
        cantidad_numero = int (cantidad)                #Convierte la string recibida a un numero entero
        cantidad_total_doritos = lista[1] + cantidad_numero
        lista[1] = cantidad_total_doritos
        costo_doritos = cantidad_numero * DORITOS_PRECIO    #Operacion que obtiene el costo del producto en base a la cantidad y el precio unitario
        print ("Costo", costo_doritos)      
        seguir = input ("Seguir comprando [y/n]")       
        if seguir == "n":                               #If para saber si se quiere seguir comprando o no
            costo_doritos_total += costo_doritos        #Variable que con una suma va a ir acumulando el costo de todos los productos adquiridos
            cantidad_numero_total += cantidad_numero    #Variable que con una suma va a ir acumulando la cantidad de prodcutos adquiridos
            costo_total += costo_doritos_total          #Variable que con una suma va a ir acumulando la cantidad del costo total 
            i = i + 1                                   #En caso de no querer seguir comprando se detiene el cilco while sumandole una unidad a "i"
            recibo (presupuesto_numero)                 #Se activa la funcion que creara el recibo de la compra
        elif seguir == "y":                             #En caso de seguir comprando el if seguira este algoritmo
            costo_doritos_total += costo_doritos        #Variable que con una suma va a ir acumulando el costo de todos los productos adquiridos
            cantidad_numero_total += cantidad_numero     #Variable que con una suma va a ir acumulando la cantidad de prodcutos adquiridos
            costo_total += costo_doritos_total          #Variable que con una suma va a ir acumulando la cantidad del costo total 
            i = i                                       #Al querer seguir comprando se repetira el ciclo while
    elif seleccion == "3":                              #Un if para saber que producto se va a comprar
        cantidad = input ("Cuantos vas a comprar: ")    #Se solicita el numero de productos que se van a comprar
        cantidad_numero = int (cantidad)                #Convierte la string recibida a un numero entero
        cantidad_total_paleta = lista[2] + cantidad_numero
        lista[2] = cantidad_total_paleta
        costo_paleta = cantidad_numero * PALETA_PAYASO_PRECIO   #Operacion que obtiene el costo del producto en base a la cantidad y el precio unitario
        print ("Costo", costo_paleta)                   
        seguir = input ("Seguir comprando [y/n]")
        if seguir == "n":                               #If para saber si se quiere seguir comprando o no
            costo_paleta_total += costo_paleta          #Variable que con una suma va a ir acumulando el costo de todos los productos adquiridos
            cantidad_numero_total += cantidad_numero    #Variable que con una suma va a ir acumulando la cantidad de prodcutos adquiridos
            costo_total += costo_paleta_total           #Variable que con una suma va a ir acumulando la cantidad del costo total
            i = i + 1                                   #En caso de no querer seguir comprando se detiene el cilco while sumandole una unidad a "i"
            recibo (presupuesto_numero)                 #Se activa la funcion que creara el recibo de la compra
        elif seguir == "y":                             #En caso de seguir comprando el if seguira este algoritmo
            costo_paleta_total += costo_paleta          #Variable que con una suma va a ir acumulando el costo de todos los productos adquiridos
            cantidad_numero_total += cantidad_numero    #Variable que con una suma va a ir acumulando la cantidad de prodcutos adquiridos
            costo_total += costo_paleta_total           #Variable que con una suma va a ir acumulando la cantidad del costo total
            i = i                                       #Al querer seguir comprando se repetira el ciclo while
    elif seleccion == "4":                              #Un if para saber que producto se va a comprar
        cantidad = input ("Cuantos vas a comprar: ")    #Se solicita el numero de productos que se van a comprar
        cantidad_numero = int (cantidad)                #Convierte la string recibida a un numero entero
        cantidad_total_agua = lista[3] + cantidad_numero
        lista[3] = cantidad_total_agua
        costo_agua = cantidad_numero * botella_agua_precio_determinado  #Operacion que obtiene el costo del producto en base a la cantidad y el precio unitario
        print ("Costo", costo_agua)
        seguir = input ("Seguir comprando [y/n]")
        if seguir == "n":                               #If para saber si se quiere seguir comprando o no
            costo_agua_total += costo_agua              #Variable que con una suma va a ir acumulando el costo de todos los productos adquiridos
            cantidad_numero_total += cantidad_numero    #Variable que con una suma va a ir acumulando la cantidad de prodcutos adquiridos
            costo_total += costo_agua_total             #Variable que con una suma va a ir acumulando la cantidad del costo total
            i = i + 1                                   #En caso de no querer seguir comprando se detiene el cilco while sumandole una unidad a "i"
            recibo (presupuesto_numero)                 #Se activa la funcion que creara el recibo de la compra
        elif seguir == "y":                             #En caso de seguir comprando el if seguira este algoritmo
            costo_agua_total += costo_agua              #Variable que con una suma va a ir acumulando el costo de todos los productos adquiridos
            cantidad_numero_total += cantidad_numero    #Variable que con una suma va a ir acumulando la cantidad de prodcutos adquiridos
            costo_total += costo_agua_total             #Variable que con una suma va a ir acumulando la cantidad del costo total
            i = i                                       #Al querer seguir comprando se repetira el ciclo while
    elif seleccion == "5":                              #Un if para saber que producto se va a comprar
        cantidad = input ("Cuantos vas a comprar: ")    #Se solicita el numero de productos que se van a comprar
        cantidad_numero = int (cantidad)                #Convierte la string recibida a un numero entero
        cantidad_total_cacahuate = lista[4] + cantidad_numero
        lista[4] = cantidad_total_cacahuate
        costo_cacahuate = cantidad_numero * cacahuates_premium_precio   #Operacion que obtiene el costo del producto en base a la cantidad y el precio unitario
        print ("Costo", costo_cacahuate)                
        seguir = input ("Seguir comprando [y/n]")
        if seguir == "n":                               #If para saber si se quiere seguir comprando o no
            costo_cacahuate_total += costo_cacahuate    #Variable que con una suma va a ir acumulando el costo de todos los productos adquiridos
            cantidad_numero_total += cantidad_numero    #Variable que con una suma va a ir acumulando la cantidad de prodcutos adquiridos
            costo_total += costo_cacahuate_total        #Variable que con una suma va a ir acumulando la cantidad del costo total
            i = i + 1                                   #En caso de no querer seguir comprando se detiene el cilco while sumandole una unidad a "i"
            recibo (presupuesto_numero)                 #Se activa la funcion que creara el recibo de la compra
        elif seguir == "y":                             #En caso de seguir comprando el if seguira este algoritmo
            costo_cacahuate_total += costo_cacahuate    #Variable que con una suma va a ir acumulando el costo de todos los productos adquiridos
            cantidad_numero_total += cantidad_numero    #Variable que con una suma va a ir acumulando la cantidad de prodcutos adquiridos
            costo_total += costo_cacahuate_total        #Variable que con una suma va a ir acumulando la cantidad del costo total
            i = i                                       #Al querer seguir comprando se repetira el ciclo while

