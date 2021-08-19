""" * store and reduce
a los programadores no nos gusta repertirnos XD
como las variables, las funciones quedan guardas en memoria durante el runtime
tiene declaracion e invocacion o llamar
recordas estas funciones?? 

print()
input()
type()     

conversion de tipo de dato
float()
int()
str()

estas son built-in  durante este capitulo veremos algunas mas

Python proporciona un número importante de funciones internas, que pueden ser
usadas sin necesidad de tener que definirlas previamente. Los creadores de Python
han escrito un conjunto de funciones para resolver problemas comunes y las han
incluido en Python para que las podamos utilizar.

"""

"""
hablemos de return: len() min() max() son funciones que nos retornan un dato en base al que recibieron como parametro
max() nos devuelve el mayor valor
min() nos devuelve el menor valor
len() nos duelve el largo de la cadena de caracteres

el resultado de una funcion se puede guardar en una variable dado que al invocarna nos devuelve un resultado.

podemos anidar las funciones. asi al tener el retorno de una funcion lo usamos como parametro para otra funcion
! mostrar ejemplo
"""

# vector1 = 'hola mundo!'
# vector2 = [3,123, 53,1,52]
# vector3 = ['juan','pedro','max']

# x = min(vector1)
# print(x)

# print(min(vector2))
# print(max(vector3))
# print(len(vector1))

"""
funciones matematicas

Python tiene un módulo matemático (math), que proporciona la mayoría de las
funciones matemáticas habituales. Antes de que podamos utilizar el módulo, deberemos
importarlo.

El objeto módulo contiene las funciones y variables definidas en el módulo. Para
acceder a una de esas funciones, es necesario especificar el nombre del módulo y el
nombre de la función, separados por un punto. Este formato recibe el nombre de notación punto.

"""
# import math
# print(math)

# raiz = math.sqrt(2)
# print(raiz)

# numero_truncado = math.floor(raiz)
# print(numero_truncado)

# print(math.factorial(6))


# import random

# for i in range(10):
#   x,y,z = random.random(), random.randint(5, 10), random.choice(vector1)
#   print(x,y,z)
"""
creando nuestra funciones

def nombre_de_la_funcion():
    "hace algo"
 
a estas funciones se les dice Void o vacia ya que no retornan un valor.

"""

# def muestra_estribillo():
#     print('Soy un leñador, qué alegría.')
#     print('Duermo toda la noche y trabajo todo el día.')

# print(muestra_estribillo)
# # <function muestra_estribillo at 0x000001875F305160>
# print(type(muestra_estribillo))
# # <type 'function'>

# muestra_estribillo()

# def repite_estribillo():
#     muestra_estribillo()
#     muestra_estribillo()

# repite_estribillo()

"""
argumentos y alcanze de la variables
las funciones pueden recibir argumentos que van dentro de los () al invocarla
print() recibe como argumento un string o una variable y nos retorna por consula un valor
dir() recibe un objeto y devuelve sus propiedades y metodos.

creemos una funcion que reciba parametros y nos devuelva un resultado distinto segun el parametro
"""

# def saludo(lang) :
#     if lang == 'es':
#         return 'Hola '
#     elif lang == 'jap':
#         return 'こんにちは世界' #こんにちは世界 == konnichiwa
#     else:
#         return 'Hello '

# print(saludo('es'))
# print(saludo('jap'))
# print(saludo('it'))

"""
para entender mejor la diferencias entre funciones void y funciones q devulven un valor
funciones productivas e improductivas

"""
# # void
# def muestra_dos_veces(x):
#     print(x)                         
#     print(x)

# resultado = muestra_dos_veces('Bing')
# print(resultado)
# # con return

# def sumados(a, b):
#     suma = a + b
#     return suma # o directamente a + b

# x = sumados(3, 5)
# print(x)


"""
COnceptos de las funciones e idea de funciones

• El crear una función nueva te da la oportunidad de dar nombre a un grupo
de sentencias, lo cual hace tu programa más fácil de leer, entender y depurar.

• Las funciones pueden hacer un programa más pequeño, al eliminar código
repetido. Además, si quieres realizar cualquier cambio en el futuro, sólo
tendrás que hacerlo en un único lugar.

• Dividir un programa largo en funciones te permite depurar las partes de una
en una y luego ensamblarlas juntas en una sola pieza.

• Las funciones bien diseñadas a menudo resultan útiles para otros muchos
programas. Una vez que has escrito y depurado una, puedes reutilizarla.
"""

""" 
Ejercicio 1: Reescribe el programa de cálculo del salario, con tarifa-ymedia
para las horas extras, y crea una función llamada calculo_salario
que reciba dos parámetros (horas y tarifa).

Ejercicio 2: Reescribe el programa de calificaciones del capítulo anterior
usando una función llamada calcula_calificacion, que reciba una
puntuación como parámetro y devuelva una calificación como cadena.
"""