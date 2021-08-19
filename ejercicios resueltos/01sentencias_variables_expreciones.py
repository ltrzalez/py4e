"""
Ejercicio 1: ¿Qué está mal en el siguiente código?:
     primt '¡Hola, mundo!'
""" 
# print('¡Hola, mundo!')

"""
Ejercicio 2: ¿Qué mostrará en pantalla el siguiente programa?:
    x = 43
    x = x + 1
    print(x)

    44
"""

"""
Ejercicio 3: 

Desired Output
hello world
"""
# print('¡Hola, mundo!')

"""
Ejercicio 4: Asume que ejecutamos las siguientes sentencias de asignación:
ancho = 17
alto = 12.0
Para cada una de las expresiones siguientes, escribe el valor de la expresión y el
tipo (del valor de la expresión).
1. ancho/2  float
2. ancho/2.0 float
3. alto/3 float 
4. 1 + 2 * 5 int
Usa el intérprete de Python para comprobar tus respuestas.
"""
ancho = 17
alto = 12.0
print(type(ancho))
print(type(alto))

a = ancho / 2
b = ancho / 2.0
c = alto / 3
d = 1 + 2 *5

print(a)
print(type(a))
print(b)
print(type(b))
print(c)
print(type(c))
print(d)
print(type(d))



"""
Ejercicio 5. Ascensor.
Dado que en europa el piso mas bajo es 0 y en estados unidos ese mismo piso es 1.
Escriba un programa que pregunta al usuario un piso en europa y responda que piso es en estados unidos
*pensa que todo programa basicamente es input -> proceso -> output.
podes escribir una linea para cada paso, para resolver este ejercicio
"""
# lo tengo 


"""
Ejercicio 6 calculadora de parking
pregunta al usuario horas y costo de la hora, el programa debe responder el total en formato "Costo: total"
You should use input to read a string and float() to convert the string to a number.
Do not worry about error checking or bad user data.

"""

# horas = float(input("Cuantas horas :"))
# tarifa = float(input("A que precio :"))
# total = horas * tarifa

# print("Pay: " + str(total))
#print("Pay:", str(total))

"""
Ejercicio 7: Escribe un programa que le pida al usuario una temperatura
en grados Celsius, la convierta a grados Fahrenheit e imprima
por pantalla la temperatura convertida.
"""
# tempcelcius = input('Ingrese temperatura en Celcius\n')
# try:
#     res = (float(tempcelcius) * 9 / 5 + 32)
#     print((res), 'Fahreinheit')
# except:
#     print('Por favor, ingrese un valor numerico')
#     tempcelcius = input('Ingrese temperatura en Celcius\n')
#     res = (float(tempcelcius) * 9 / 5 + 32)
#     print((res), 'Fahreinheit')