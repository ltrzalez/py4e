""" ejercicios

Ejercicio 1: Reescribe el programa del cálculo del salario para darle al empleado
1.5 veces la tarifa horaria para todas las horas trabajadas que excedan de 40.

Introduzca las Horas: 45
Introduzca la Tarifa por hora: 10
Salario: 475.0 """

# hrs = input("Enter Hours:")
# horas = float(hrs)
# price = input("Enter price:")
# p = float(price)

# if horas > 40:
#     normal = horas * p
#     extra = (horas - 40) * (p * 0.5)
#     output = normal + extra
#     print(output)
# else:
#     output = horas * p
#     print(output)


""" Ejercicio 2: Reescribe el programa del salario usando try y except, de modo que el
programa sea capaz de gestionar entradas no numéricas con elegancia, mostrando
un mensaje y saliendo del programa. A continuación se muestran dos ejecuciones
del programa:

Introduzca las Horas: 20
Introduzca la Tarifa por hora: nueve
Error, por favor introduzca un número

Introduzca las Horas: cuarenta
Error, por favor introduzca un número  """ 

# try:
#     hrs = input("Enter Hours:")
#     horas = float(hrs)
#     price = input("Enter price:")
#     p = float(price)
#     if horas > 40:
#         normal = horas * p
#         extra = (horas - 40) * (p * 0.5)
#         output = normal + extra
#         print(output)
#     else:
#         output = horas * p
#         print(output)
# except:
#     print('Error, por favor introduzca un número')


"""

Ejercicio 3: Escribe un programa que solicite una puntuación entre 0.0 y 1.0. Si la
puntuación está fuera de ese rango, muestra un mensaje de error. Si la puntuación
está entre 0.0 y 1.0, muestra la calificación usando la tabla siguiente:

"""

# score = input("Enter Score: ")

# try:
#     calif = float(score)
# except:
#     print('error')
#     exit()
# if calif >= 0.9 :
#     print('A')
# elif calif >= 0.8 :
#     print('B')
# elif calif >= 0.7 :
#     print('C')
# elif calif >= 0.6 :
#     print('D')
# elif calif < 0.6 :
#     print('F')
