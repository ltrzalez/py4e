# iteraciones o bucles o for and while
"""
Con las iteraciones podemos hacer que los programas se repitan hasta lograr algo
hasta ahora solo lo hacian una vez.

Éste es el flujo de ejecución de la sentencia while:
1. Se evalúa la condición, obteniendo Verdadero or Falso.
2. Si la condición es falsa, se sale de la sentencia while y se continúa la ejecución
en la siguiente sentencia.
3. Si la condición es verdadera, se ejecuta el cuerpo del while y luego se vuelve
al paso 1.
Cada vez que se ejecuta el cuerpo del bucle se dice que realizamos
una iteración.

"""


# numero = 5
# while numero > 0:
#     print(n)
#     n = n -1 # n -= 1
# print('fin')
# print(n)


"""
maneras de controlar la iteracion
mientras la condcion del argumento sea verdadera se ejecutara
break => corta la ejucion del bucle
continue => corta el flujo del bucle y vuelve al principio
pass => sigue el flujo de ejecucion 
"""

# while True:
#     entrada = input('> ')
#     if entrada == 'fin':
#         break
#     print(entrada)
# print('fin')

# while True:
#     entrada = input('> ')
#     if entrada[0] == '#':
#         continue
#     if entrada == 'fin':
#         break
#     print(entrada)
# print('fin')


""" loops infinitos vs loops finitos (mientras vs iteracion) """

# for i in [5, 4, 3, 2, 1] : # range(5)
#     print(i)
# print('fin')

# amigos = ['cadabra']
# for amigo in amigos:
#     print('hola ' + amigo)

""" ejemplos js
let amigos = ['choco','manu','belu'] 
amigos.forEach( amigo => console.log('hola ' +amigo))
"""
""" making "smart" loop 

Los bucles generalmente se construyen así:
• Se inicializan una o más variables antes de que el bucle comience
• Se realiza alguna operación con cada elemento en el cuerpo del bucle, posiblemente
cambiando las variables dentro de ese cuerpo.
• Se revisan las variables resultantes cuando el bucle se completa


"""

# el_numero_mas_grande = 0
# print('antes del loop')
# for un_numero in [1,5,3,523,86,3] :
#     if un_numero > el_numero_mas_grande:
#         el_numero_mas_grande = un_numero
#     print(un_numero, el_numero_mas_grande)
# print('despues del loop el numero mas grande es :' + str(el_numero_mas_grande))

# ejercicios: nombre un metodo que encuentra el mayor numero de una lista   

""" loops para contar, para sumar totales, para sacar promedios.
tenes ejemplo de contar y sumar el valor total. Crea uno para obtener el promedio 

"""

# contador = 0
# for valor in [3, 41, 12, 9, 74, 15]:
#     contador = contador + 1
# print('Num. elementos: ', contador)


# total = 0
# for valor in [3, 41, 12, 9, 74, 15]:
#     total = total + valor
# print('Total: ', total)


# filtrando dentro del loop para buscar un cosa o algun patron. TO DO exportar la funcion de las notas de los alumnos

# menor = None
# for value in [21,35,32,3,5,123,4] :
#     if menor is None :
#         menor = value
#     elif value < menor:
#         menor = value
#     print(menor, value)

# print('el menor es', str(menor))


# !!! diferencia y similitud entre "is & ==" y "is not & !=" valor y valor y tipos


"""" 
Ejercicio 1: Escribe un programa que lea repetidamente números hasta
que el usuario introduzca “fin”. Una vez se haya introducido “fin”,
muestra por pantalla el total, la cantidad de números y la media de
esos números. Si el usuario introduce cualquier otra cosa que no sea un
número, detecta su fallo usando try y except, muestra un mensaje de
error y pasa al número siguiente.


Ejercicio 2: Escribe otro programa que pida de a un numero, que al recibir "done" termine el programa,
que responda "invalid input" cuando no sea un numero y muestre por pantalla el máximo y mínimo de los
números.

"""
num = 0
suma = 0
media = 0
try:
    while True:
        entrada = int(input('Ingrese palabra: '))
        num = num + 1
        suma = suma + entrada
        media = suma / num
        if entrada != 'fin':
            continue
        if entrada == 'fin':
            break
except ValueError:
    print('Introduzca otro numero si desea continuar.')
    print('A continuacion se detalla lo ingresado')
    print('El contador llego a:', num)
    print('La suma total es:', suma,)
    print('La media es:', int(media))        


 