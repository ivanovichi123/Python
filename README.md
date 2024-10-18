# Compras

En algún momento, todos hemos necesitado una forma efectiva de recordar qué productos comprar. Las listas de compras nos ayudan a organizar nuestras necesidades y asegurarnos de no olvidar nada importante. Tradicionalmente, estas listas se hacían en papel, pero en un mundo digital, las notas en papel están siendo reemplazadas por aplicaciones y herramientas digitales que ofrecen mayor facilidad al hacer notas o analizar información. En un mundo cada vez más digital, dejar de usar notas en papel y empezar a usar tecnologías es esencial. Las herramientas digitales no solo nos facilitan la tarea de comparar precios, sino que también nos permiten llevar un seguimiento detallado de nuestros gastos y ajustar nuestro presupuesto en tiempo real.     

Por lo tanto, la transición de notas en papel a herramientas digitales no solo facilita nuestras compras, sino que también nos permite ser consumidores más informados y eficientes. La capacidad de comparar precios y llevar un seguimiento detallado de nuestros gastos en tiempo real nos proporciona un mayor control sobre nuestras finanzas y nos ayuda a hacer compras más inteligentes y conscientes. Adoptar estas tecnologías no solo mejora nuestra organización y eficiencia, sino que también nos permite aprovechar al máximo nuestro tiempo y recursos, haciendo de nuestras experiencias de compra algo más cómodo y efectivo.

## ¿Por que es interesante?
- Las herramientas digitales nos permiten hacer nuestras compras de manera más rápida y organizada.
- Comparar precios y gestionar nuestro presupuesto de manera eficiente nos ayuda a ahorrar dinero.
- Planificar nuestras compras y ser conscientes de nuestro presupuesto también puede contribuir a la sostenibilidad.
-  Al tener una lista de compras organizada y accesible, puedes ahorrar tiempo al evitar olvidos y vueltas innecesarias al supermercado.

## Algoritmo (para un solo producto)
**Inicio**  
    &emsp;presupuesto <- input ("¿Cual es su presupuesto?: ")  
    &emsp;presupuesto_numero <- int(presupuesto)  
    &emsp;REFRESCO_PRECIO <- 20  
    &emsp;DORITOS_PRECIO <- 23  
    &emsp;PALETA_PRECIO <- 10  
    &emsp;print("[1]Refresco coca cola ($20)")  
    &emsp;print ("[2]Doritos ($23)")  
    &emsp;print ("[3]Paleta payaso ($10)")  
    &emsp;seleccion <- input("Selecciona el numero del articulo que vas a comprar: ")  
       &emsp;**Si seleccion es igual a "1":**  
         &emsp;&emsp;cantidad <- input("Cuantos vas a comprar: ")  
         &emsp;&emsp;cantidad_numero <- int(cantidad)  
         &emsp;&emsp;costo <- cantidad_numero * refresco_precio  
         &emsp;&emsp;print ("Costo", costo)  
         &emsp;&emsp;seguir <- input ("Seguir comprando [y/n]")  
          &emsp;&emsp;**Si seguir es igual a "n":**  
            &emsp;&emsp;&emsp;print ("Recibo:")  
            &emsp;&emsp;&emsp;print ("Productos comprados: ", cantidad_numero)  
            &emsp;&emsp;&emsp;print ("Presupuesto: ", presupuesto_numero)  
            &emsp;&emsp;&emsp;print ("Costo total: ", costo)  
            &emsp;&emsp;&emsp;cambio <- presupuesto_numero - costo  
            &emsp;&emsp;&emsp;print ("Cambio: ", cambio)  
            &emsp;&emsp;**Sino repetir todo el proceso desde seleccionar el numero del articulo que se va a comprar**  
&emsp;**Sino checar si es igual a "2" o "3" y repetir el mismo proceso que en "1"**  

## Características
- Permite al usuario seleccionar entre varios productos (refrescos, doritos, paletas payaso, botellas de agua y cacahuates premium).
- Calcula el costo total de los productos adquiridos.
- Genera un recibo al finalizar la compra, que incluye la lista de productos comprados, el costo total y el cambio del presupuesto.
- Verifica que el presupuesto ingresado sea un número válido.
- Admite múltiples compras hasta que el usuario decida finalizar.

## Productos Disponibles
- Refresco Coca Cola: $20
- Doritos: $23
- Paleta Payaso: $10
- Botella de Agua: Precio variable según mes y semana.
- Cacahuates Premium: Precio variable según mes y semana.

## Variables Constantes
- REFRESCO_PRECIO: Precio del refresco ($20).
- DORITOS_PRECIO: Precio de los doritos ($23).
- PALETA_PAYASO_PRECIO: Precio de la paleta payaso ($10).

## Variables de Costo
- costo_refresco_total: Acumula el costo total de los refrescos comprados.
- costo_doritos_total: Acumula el costo total de los doritos comprados.
- costo_paleta_total: Acumula el costo total de las paletas payaso compradas.
- costo_agua_total: Acumula el costo total del agua comprada.
- costo_cacahuate_total: Acumula el costo total de los cacahuates comprados.
- cantidad_total: Acumula la cantidad total de productos adquiridos.
- costo_total: Acumula el costo total de la compra.

## Funciones Principales
- recibo(presupuesto_numero): Imprime un recibo detallado de la compra.
- es_numero(presupuesto): Verifica si el presupuesto ingresado es un número.
- determina_cacahuate_agua_precio(mes, semana): Determina el precio de los cacahuates y el agua según el mes y la semana.

## Uso
1. Ejecuta el archivo de Python.
2. Ingresa el mes y la semana de la compra.
3. Especifica tu presupuesto.
4. Selecciona los productos que deseas comprar ingresando el número correspondiente.
5. Indica la cantidad de cada producto que deseas adquirir.
6. Decide si deseas seguir comprando o finalizar la compra.
7. Al finalizar, el recibo se imprimirá con todos los detalles.

## Variable global
El comando "global" se utiliza para permitir que una variable dentro de una función modifique una variable definida a nivel global en el programa. Sin "global", cualquier variable creada
dentro de una función sería local a esa función, y los cambios no afectarían la variable global. En el código, "global" se usa para asegurarse de que los cambios en variables "a" y
"presupuesto_numero" dentro de la función se reflejen en todo el programa, permitiendo controlar el ciclo y el manejo del presupuesto de manera correcta.

## f-strings
Los f-strings en Python se utilizan para combinar texto con variables en una cadena. Se utilizan añadiendo una "f" antes de las comillas y colocando las
variables o expresiones entre llaves. Este método permite crear cadenas con variables de manera sencilla y rápida. Los f-strings mejoran la legibilidad del código y son una herramienta
valiosa para formar texto en Python.

## Refrerencias 
- W3Schools.com. (s. f.). https://www.w3schools.com/python/
- W3Schools.com. (s. f.-b). https://www.w3schools.com/python/python_variables_global.asp
- GeeksforGeeks. (2024, 19 junio). fstrings in Python. GeeksforGeeks. https://www.geeksforgeeks.org/formatted-string-literals-f-strings-python/
