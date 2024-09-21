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
        

while a == 0:                                               #ciclo "while", que se repite si no se da un valor numerico como presupuesto
    presupuesto = input ("¿Cual es su presupuesto?: ")      #Pide el presupuesto de la persona
    print ("Tu presupuesto es de: ",es_numero(presupuesto)) #Imprime el resultado de la funcion "es_numero"


while i == 0:                                       #Incio del ciclo while
    print ("[1]Refresco coca cola ($20)")           #Los distintos productos que se pueden escoger
    print ("[2]Doritos ($23)")
    print ("[3]Paleta payaso ($10)")
    print ("[4]Botella de agua ($13)")
    print ("[5]Cacahuates premium ($30)")
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
        costo_agua = cantidad_numero * BOTELLA_AGUA_PRECIO  #Operacion que obtiene el costo del producto en base a la cantidad y el precio unitario
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
        costo_cacahuate = cantidad_numero * CACAHUATES_PREMIUM_PRECIO   #Operacion que obtiene el costo del producto en base a la cantidad y el precio unitario
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
