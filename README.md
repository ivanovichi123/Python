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


