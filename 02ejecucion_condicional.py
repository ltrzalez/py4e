
# *condicional todo hacer los pptx de estos ejemplos y agregar ejercicio. ejercicios de este capitulo seran utilizados en el proximo

# """ Ejecucion condicional """
""" usaremos la palabra reservada if, elif, para que python tome 'decisiones'
al chekiar si una condicion es verdadera o falsa """

""" Tipo de dato Booleano, pueden ser Verdadeo o falso """
# print(5 == 5)
# True
# print(5 == 6)
# False

""" operadores de comparacion """ 

# x != y # x es distinto de y
# x > y # x es mayor que y
# x < y # x es menor que y
# x >= y # x es mayor o igual que y
# x <= y # x es menor o igual que y
# x is y # x es lo mismo que y
# x is not y # x no es lo mismo que y

""" Operadores lógicos
Existen tres operadores lógicos: and (y), or (o), y not (no). El significado
semántico de estas operaciones es similar a su significado en inglés.
"""
#  suponer valores de las variables para entender cuando son verdaros o falso

# x > 0 and x < 10

# n%2 == 0 or n%3 == 0

# not (x > y)


""" una simple  """

# if x > 0 :
#     print('x es positivo')


""" tomamos un solo camino cada vez que chekiamos la condicion. Hablar de la importancia de la identacion  """

# x = 5
# if x < 18:
#     print('menor')
# if x > 18:
#     print('adulto')

""" dos deciciones. Else y porque no lleva parametro de condicional """

# if x%2 == 0 :
#    print('x es par')
# else :
#    print('x es impar')


""" condicionales encadenados """

# if x < y:
#     print('x es menor que y')
# elif x > y:
#     print('x es mayor que y')
# else:
#     print('x e y son iguales')


""" condicionales anidados y mas identacion """ 

# if 0 < x:
#     if x < 10:
#         print('x es un número positivo con un sólo dígito.')

# if x == y:
#   print('x e y son iguales')
# else:
#    if x < y:
#       print('x es menor que y')
#   else:
#        print('x es mayor que y')



""" varios caminos de decicion elif y la no utilizacion de else y la importancia del orden """

#  agregar variante que falta para que funcione

# if choice == 'a':
#    print('Respuesta incorrecta')
# elif choice == 'b':
#    print('Respuesta correcta')
# elif choice == 'c':
#    print('Casi, pero no es correcto')

""" try and except y operador ternario """ 

# ent = input('Introduzca la Temperatura Fahrenheit:')
# try:
#     fahr = float(ent)
#     cel = (fahr - 32.0) * 5.0 / 9.0
#     print(cel)
# except:
#     print('Por favor, introduzca un número la proxima vez')

# try:
#     print('x' if True else 'nada')
# except:
#     pass

""" operador ternario en js """
# try{
#     console.log(true ? 'x' : 'nada')
# }
# catch{
#     console.log('error')
# }


""" ejercicios

Ejercicio 1: Reescribe el programa del cálculo del salario para darle al empleado
1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40.

Introduzca las Horas: 45
Introduzca la Tarifa por hora: 10
Salario: 475.0

Ejercicio 2: Reescribe el programa del salario usando try y except, de modo que el
programa sea capaz de gestionar entradas no numéricas con elegancia, mostrando
un mensaje y saliendo del programa. A continuación se muestran dos ejecuciones
del programa:

Introduzca las Horas: 20
Introduzca la Tarifa por hora: nueve
Error, por favor introduzca un número

Introduzca las Horas: cuarenta
Error, por favor introduzca un número

Ejercicio 3: Escribe un programa que solicite una puntuación entre 0.0 y 1.0. Si la
puntuación está fuera de ese rango, muestra un mensaje de error. Si la puntuación
está entre 0.0 y 1.0, muestra la calificación usando la tabla siguiente:


"""
