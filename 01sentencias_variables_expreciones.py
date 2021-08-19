"""
*secuencial

Python (como todo lenguaje de programacion) tiene Keywords, que tiene un significado especial para el interprete
Estas son las palbras reservadas

and del global not with as elif if or yield assert else import pass break except in raise
class finally is return continue for lambda try def from nonlocal while

funciones integradas (built-in es como dicen en ingles en los docs)
 en python tambien se pueden considerar palabras reservadas Ej.: print()
que palabras son reservadas en las 2 proximas lineas de codigo """

# for slice in pizza:
#   print(slice)

""" si ejecutamos este programa escribiendo en la consola 'python nombre_del_archivo.py' veremos hola mundo en la consola """
# print('hola mundo')

"""podemos ejecutar el mismo codigo sin la necesidad de escribrir un programa
Lo haremos ejecutando el interprete de python en la consola con el comando python
(para terminar la ejecucion lo haremos con la funcion quit() o exit()) """

# un programa es una secuencia de pasos, algunos son condicionales otros repetivos
# a veces guardas una serie de pasos porque lo vas a usar varias veces a lo largo del script

#Variables
""" almacenan datos en memoria. Se les asigna un nombre y un valor. """
# x = 2 # sentencia de asignacion
# x = x + 2 # asignacion con exprecion ( + - / *  ** %) (and or not is)
# print(x) # exprecion

# x = 2 
# y = 12.2
# print(x)
# print(y)
# x, y = y, x 


""" typos de datos 
int() str() float()  no se pueden sumar numeros y letras.
Enteros cadena de caracteres y numeros con coma(respectivamente)
consulta el tipo de dato con la siguiente funcion
"""
# type(variable) 

# numero = 2
# print(numero)

# print(float(numero))

# con_coma = float(numero)
# string = 'vamos los pibes'

# print(str(con_coma))
# print(int(string))

# print(1,000,000)

""" operacion de cadenas y enteros """
#  primero = 10
#  segundo = 15
#  print(primero+segundo)

#  primero = '100'
#  segundo = '150'
#  print(primero + segundo)

""" input esperamos un dato desde la consola mientras se ejecuta el script. input() retorna un str """
# nombre = input('¿como te llamas? \n')
# print('hola ' + nombre)

"""Elijamos un nombre correcto para las variables, no como en este ejemplo(para saber el pago = horas x precio)"""
# qdac2r = 35.00
# dqac3r = 12.50
# acqd2s = qdac2r * dqac3r
# print(acqd2s)

""" en python se estila snake_case en vez de camelCase """


""" Depuracion(debuging) es el proceso de quitar errores de los programas.
Miremos algunos ejemplos de como el interprente de python nos comunica los errores. """  

# month = 09

# bad name = 5

# principal = 327.68
# interest = principle * rate



""" En los siguientes capitulos veremos condicionales y bucles
asi que echemos un vistaso antes de los ejercios de esta unidad """
"""  Ejercicio, reconocer, condicionales y repeticiones """

# name = input('Enter file:')
# handle = open(name, 'r')

# counts = dict()
# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1

# bigcount = None
# bigword = None
# for word, count in list(counts.items()):
#     if bigcount is None or count > bigcount:
#     bigword = word
#     bigcount = count

# print(bigword, bigcount)

"""
Ejercicio 1: ¿Qué está mal en el siguiente código?:
     primt '¡Hola, mundo!'


Ejercicio 2: ¿Qué mostrará en pantalla el siguiente programa?:
    x = 43
    x = x + 1
    print(x)

Ejercicio 3: 

Desired Output
hello world

Ejercicio 4: Asume que ejecutamos las siguientes sentencias de asignación:
ancho = 17
alto = 12.0
Para cada una de las expresiones siguientes, escribe el valor de la expresión y el
tipo (del valor de la expresión).
1. ancho/2
2. ancho/2.0
3. alto/3
4. 1 + 2 * 5
Usa el intérprete de Python para comprobar tus respuestas.

Ejercicio 5. Ascensor.
Dado que en europa el piso mas bajo es 0 y en estados unidos ese mismo piso es 1.
Escriba un programa que pregunta al usuario un piso en europa y responda que piso es en estados unidos
*pensa que todo programa basicamente es input -> proceso -> output.
podes escribir una linea para cada paso, para resolver este ejercicio


Ejercicio 6 calculadora de parking
pregunta al usuario horas y costo de la hora, el programa debe responder el total en formato "Costo: total"
You should use input to read a string and float() to convert the string to a number.
Do not worry about error checking or bad user data.

Ejercicio 7: Escribe un programa que le pida al usuario una temperatura
en grados Celsius, la convierta a grados Fahrenheit e imprima
por pantalla la temperatura convertida.

"""