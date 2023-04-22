### 1. Operaciones de orden con 3 nros. 

Realizar un programa que tome tres números, los ordene de mayor a menor, y diga si el tercero es el resto de la división de los dos primeros.

### 2. Elecciones Presidenciales

Según la Ley Electoral de la República Argentina, el Presidente y el Vicepresidente se eligen de acuerdo a las siguientes reglas:

Artículo 149. — Resultará electa la fórmula que obtenga más del cuarenta y cinco por ciento (45 %) de los votos afirmativos válidamente emitidos; en su defecto, aquella que hubiere obtenido el cuarenta por ciento (40 %) por lo menos de los votos afirmativos válidamente emitidos y, además, existiere una diferencia mayor de diez puntos porcentuales respecto del total de los votos afirmativos válidamente emitidos, sobre la fórmula que le sigue en número de votos.

Artículo 150. — Si ninguna fórmula alcanzare esas mayorías y diferencias de acuerdo al escrutinio ejecutado por las Juntas Electorales, y cuyo resultado único para toda la Nación será anunciado por la Asamblea Legislativa atento lo dispuesto por el artículo 120 de la presente ley, se realizará una segunda vuelta dentro de los treinta (30) días.

Artículo 151. — En la segunda vuelta participarán solamente las dos fórmulas más votadas en la primera, resultando electa la que obtenga mayor número de votos afirmativos válidamente emitidos.

Desarrollar un programa que permita ingresar, para los 3 partidos más votados: fórmula (presidente + vice) y cantidad de votos obtenidos.

Luego determinar:

-   Qué fórmula obtuvo el mayor porcentaje.
-   Si la fórmula resulta elegida o se requiere segunda vuelta. En este caso, indicar también quienes participan de la segunda vuelta.

 ### 3. Mantenimiento Informático

El Área de Mantenimiento de un laboratorio informático nos ha solicitado el desarrollo de un programa que facilite la gestión de las tareas realizadas en el día.

El usuario debe ingresar de tres equipos informáticos (PC) los siguientes datos: número de identificación de la PC, tiempo de reparación (expresado en minutos) y la causa de mantenimiento (1- Problema de Hardware 2-Problema de Software)

Los requerimientos funcionales son:

a) ¿Cuál es el tiempo total de las tareas de mantenimiento?

b) ¿Cuál es la PC (Número de identificación) que tuvo mayor tiempo en tareas de mantenimiento?

c) Tiempo promedio de tareas de mantenimiento.

d) Informar con un mensaje si todas las PC (Número de identificación) que se les ha realizado mantenimiento tuvieron problemas de Hardware.

### 4. Observatorio meteorológico

Un observatorio meteorológico ha tomado el registro de temperaturas en distintos momentos del día. Se solicita el desarrollo de un programa que facilite información estadísticas de ellas.

El usuario debe ingresar cuatro valores de temperatura (considerar que son valores enteros).

Los requerimientos funcionales son:

a) Promedio de temperatura diaria.

b) Temperatura máxima.

c) Temperatura mínima.

d) Informar con un mensaje si algunas de las temperaturas supera a la temperatura promedio.

### 5. Menú de Opciones Básico

Diseñar un programa que según la opción ingresada por el usuario permita realizar las siguientes operaciones:

-   Si la opción es 1 mostrar la superficie de un triángulo. Para calcular la superficie debe usarse la fórmula de Herón:  
    ![](data:image/png;base64,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)  
    
-   Si la opción ingresada es 2 mostrar el perímetro del triángulo.
-   Si la opción ingresada es 3 informar la longitud del lado menor.
-   Si la opción ingresada no fue ni 1, 2 o 3 informar un mensaje de error.

Para ello usted deberá ingresar por teclado el número de opción y el valor de los tres lados del triángulo.

### 6. Institución Educativa

Una institución educativa necesita un programa que facilite la gestión de cupos de los cursos de primer grado. Ingresar tres grados. De cada grado se ingresa el código de identificación (Ejemplo 1A, 1B, ...) y la cantidad de niños y de niñas y cupo máximo (que es el mismo para los tres cursos).

Los requerimientos funcionales son:

a) Código de identificación del curso que tenga menos alumnos inscriptos.

b) Porcentaje de niñas de cada curso.

c) Porcentaje de niños de cada curso.

d) Promedio general de alumnos.

e) Si algunos de los tres grados supera el cupo máximo informar un mensaje la necesidad de apertura de una nueva división.

### 7. Juego de Dados: Pares e Impares

Desarrollar un programa para simular un juego de dados con las siguientes reglas:

-   Participan 3 jugadores: el campeón y 2 retadores.
-   Antes de comenzar el juego, se debe ingresar el récord del campeón.
-   En las dos primeras rondas, compiten sólo los retadores: se lanzan 2 dados. Si la suma de ambos es impar, gana el retador 1; si no, gana el retador 2.

-   Primera ronda: el ganador obtiene tantos puntos como indica la suma de los dados
-   Segunda ronda: a los puntos de la primera ronda, el ganador suma tantos puntos como indique el dado de mayor valor, y al perdedor se le restan tantos puntos como indique el dado de menor valor

-   Ronda final: se suma a la competencia el campeón actual, que participa con un puntaje equivalente a su récord.

Se pide:

-   Mostrar en cada ronda el valor de los dados y los puntajes de cada retador.
-   Si ninguno de los retadores supera al campeón, este mantiene su puesto. En caso contrario, el que obtenga mayor puntaje será el ganador.
-   Al terminar, informar si alguno de los retadores llegó a tener más puntos que el record.
-### 8. Juego del Punto

La idea general del **_Juego del Punto_**, es lograr el máximo puntaje en 4(cuatro) vueltas de lanzamiento de 3 dados, y a continuación enumeramos las reglas en base a las cuales se obtiene puntaje:

1.) Cada jugador dispone de 4(cuatro) tiradas o lanzamientos para lograr su objetivo, el programa solo deberá simular de a una tirada por vez.

2.) En cada tirada se lanzan 3(tres) dados. _Sólo suman puntaje los dados que salgan con un punto en el centro (esto es: el 1, el 3 y el 5)_ (y de allí el nombre del juego)_._ El puntaje de la tirada se calcula sumando el aporte de cada dado, de acuerdo a las siguientes pautas:

-   Si sale el 1, se suma 1(un) punto (el único que muestra el dado).
-   Si sale el 3, se suman 2(dos) puntos (porque a los costados del punto central hay dos puntos).
-   Si sale el 5, se suman 4(cuatro) puntos (porque en este caso, hay cuatro puntos a los costados del central).
-   Si sale un número par (2, 4 o 6) no se suma ningún punto (porque ese dado no tiene punto central).

3.) Si en alguna de las tiradas el jugador saca _tres números pares iguales_, entonces el jugador duplicará los puntos finales que haya sumado al terminar sus cuatro lanzamientos.

**Se pide:** que en base a todo lo indicado, se genere un programa que simule 1 tirada de los 3 dados y luego habiendo solicitado al usuario que cargue su puntaje previo, informe su puntaje acumulado en el caso de haber obtenido puntos, su puntaje previo y el mensaje de que duplica puntos si salieron los 3 pares o simplemente su puntaje previo si no sumó ningún punto.

### 9. ¿Piedra, Papel o Tijera?

Desarrollar un programa que permita al usuario jugar contra la computadora el clásico “Piedra, Papel o Tijera” y determine cuál de ellos es el ganador.

Las reglas son:

-   La piedra aplasta (o rompe) la tijera. (Gana la piedra).
-   La tijera corta el papel. (Gana la tijera).
-   El papel envuelve la piedra. (Gana el papel)
-   Si los dos jugadores eligen el mismo elemento, empatan.

### 10. Impuesto Automotor

Crear un programa que permita calcular los impuestos que debe pagar un auto, conociendo su modelo (año de fabricación) y tipo (P: Particular/T: Taxi/R: Remis). Para calcular los impuestos, tener en cuenta que:

a. Los autos particulares de menos de 10 años de antigüedad pagan $200, entre 10 y 20 años pagan $150 y no pagan impuestos los que tienen más de 20 años.

b. Los taxis pagan impuestos como auto particular, más $150 por la licencia de taxi.

c. Los remises pagan $100 por cada año de antigüedad de su vehículo.

### 11. Calculo de Regularidad

La facultad pide un simple programa que pida las tres notas de un alumno en cualquier materia y mostrar si el alumno esta libre, regular o promocionado. Las tres notas son los dos parciales mas la nota de prácticos y las condiciones de regularidad están descriptas a continuacón:

-   El promedio menor a 4 el alumno esta libre.
-   El promedio comprendido entre 4 y 8 el alumno esta regular.
-   El promedio mayor a 8 el alumno está promocionado.

### 12. Punto en el plano

Se pide realizar un programa que ingresando el valor x e y de un punto determine a que cuadrante pertenece en el sistemas de coordenadas.

### 13. Postulantes a un empleo

Se tienen los datos de tres postulantes a un empleo a los que se les realizó un test de capacitación. Por cada postulante se tiene la siguiente información: nombre del postulante, cantidad total de preguntas que se le realizaron y cantidad de preguntas que contestó correctamente.

Se pide confeccionar un programa que lea los datos de los tres postulantes, informe el nivel de cada uno según los criterios de aprobación que se indican mas abajo, e indique finalmente el nombre del postulante que ganó el puesto. Los criterios de aprobación son los siguientes, en función del _porcentaje de respuestas correctas_ sobre el total de preguntas realizadas a cada postulante:

-   Nivel Superior: Porcentaje >= 90%
-   Nivel Medio: 75% <= Porcentaje < 90%
-   Nivel Regular: 50% <= Porcentaje < 75%
-   Fuera de Nivel: Porcentaje < 50%

### 14. Comercio

Un comerciante tiene a la venta 3 tipos de artículos principales. Conociendo la cantidad vendida de cada artículo y el precio unitario de cada artículo, hacer un programa que determine cuál fue el producto que realizó el mayor aporte en los ingresos y el porcentaje que dicho aporte significa en el ingreso absoluto de los 3 artículos sumados. Ese porcentaje se calcula así:

Absoluto ____________ 100%

Mayor aporte _________ x %

Por lo tanto: x = mayor aporte * 100 / absoluto

### 15. Pago a un Proveedor

Un comercio necesita informar el importe final a pagar a un determinado proveedor. Para ello debe ingresar la categoría (que puede ser categoría 'A' o 'B') y el importe original a abonar.

Considerar las siguientes condiciones para el cálculo del importe final a pagar:

-   Si el cliente es categoría A y el monto a pagar supera a los 1000 pesos debe aplicarse un descuento del 5%.
-   Si el cliente es categoría B y el importe a pagar oscila entre 1500 y 2500 pesos debe aplicarse un descuento del 2%.

Para ambas categorías en caso de no cumplirse las condiciones especificadas no se aplicará ningún tipo de descuento sobre el importe que se le debe abonar.

### 16. Raíces de un polinomio de segundo grado

Realizar un programa que permita calcular las raíces de un polinomio de segundo grado y mostrar un mensaje indicando si son reales o imaginarias. Si son reales distintas, mostrar sus dos valores, si son reales iguales, mostrar solo una.

_Ayudita: A partir del discriminante  _Δ_, es posible determinar la naturaleza de las raíces de la ecuación (considerando coeficientes reales) y se pueden presentar 3 situaciones:_

_• Si Δ es negativo, ambas raíces son números complejos._

_• Si Δ es igual a cero, existen dos raíces reales e iguales, por lo tanto hay una solución._

_• Si Δ es positivo, ambas raíces son reales y distintas._

### 17. Índice de Masa Corporal

Realice un programa que le permita calcular el Índice de Masa Corporal (IMC) de una persona en función de su peso (en kgs.) y su altura (en mts.), sabiendo que el IMC es igual al peso dividido la altura al cuadrado. En función del valor del IMC, el programa debe mostrar por pantalla el diagnóstico resultante del análisis del índice según las siguientes situaciones:

-   Si el IMC es menor o igual a 16: “Necesita asistencia de un médico, los riesgos para su salud son muy altos”.
-   Si el IMC es menor o igual a 17: "Usted tiene infrapeso, aliméntese más".
-   Si el IMC es menor o igual a 18: "Usted tiene bajo peso, aliméntese mejor".
-   Si el IMC es mayor a 18 y menor o igual a 26: "Usted tiene un peso saludable, continúe así!".
-   Si el IMC es mayor a 26 y menor a 30: "Tiene sobrepeso de grado I, hoy es un buen día para empezar a hacer ejercicios".
-   Si el IMC es mayor o igual a 30 y menor o igual a 35: "Tiene obesidad de grado II, necesita el apoyo de un plan nutricional".
-   Si el IMC es mayor a 35 y menor o igual a 40: "Tiene obesidad grado III (pre-mórbida), consulte con su médico los riesgos para su salud".
-   Si el IMC es mayor a 40: "Usted tiene obesidad de grado IV (mórbida), los riesgos para su salud son muy altos, consulte con su médico a la brevedad”.

### 18. Lluvias

En una localidad nos piden que realicemos un análisis de las lluvias caídas en un trimestre (3 cantidades).

Para ello se debe ingresar por teclado la cantidad de milímetros caídos por mes y con dichos datos resolver lo siguiente:

-   Promedio de milímetros caídos.
-   Cantidad de meses con más o igual lluvia que el promedio.
-   Mes con menos lluvias en el trimestre.
-   Si dicho mes tuvo 0 mm caídos indicar con un mensaje.
- 
### 19. Premio por Ventas (*)

Para calcular el premio de un vendedor, se ingresan 3 montos correspondientes a sus ventas mensuales del último trimestre.

El premio es equivalente al 50% del menor monto vendido. Si además todos los montos superan los $1000, se agrega un 10% adicional al premio calculado.

_(*) Ejercicio tipo parcial_

### 20. Análisis Estadístico

Para un análisis estadístico, se pide ingresar 3 valores y determinar:

-   Si alguno de los valores es múltiplo de 5
-   Si todos ellos son impares
-   Si el mayor de ellos supera a la suma de los otros 2
- 
### 21. Análisis Estadístico (*) - Variante

Para un análisis estadístico, se pide ingresar 3 valores y determinar:

-   Si alguno de los valores es múltiplo de 5
-   Cuántos de los valores son impares
-   Si el mayor de ellos supera a la suma de los otros 2

_(*) Ejercicio tipo parcial_

### 22. Votación en el Senado (*)

Se vota una ley en el Senado, y se ingresan votos a favor, en contra y abstenciones de los senadores presentes.

Informar cuál fue el resultado de la votación. Si la ley fue aprobada, indicar si fue por mayoría absoluta (más del 50% de los votos) o por mayoría simple.

Por último, considerando que la Cámara está formada por 72 senadores, determinar cuantos se encontraban ausentes.

_(*) Ejercicio tipo parcial_

### 23. Triatlón del Ironman

Una empresa de estadisticas nos solicito un programa sencillo que nos permita obtener los resultados de una competencia del Triatlon Ironman. Dicho programa debe cargar, a modo de prueba, los nombres y tiempos de 3 competidores expresados en hh:mm:ss (Considerar que si la hora, minuto o segundo es menor a 10 agregarle un cero al inicio), a partir de esa carga determinar:

1 - El tiempo promedio entero de la prueba  
2 - Mostrar como quedo conformado el podio en base a esos tres tiempos  
3 - Indicar con un mensaje, si el tiempo ganador fue superior al tiempo promedio de la prueba