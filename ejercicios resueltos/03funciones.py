""" 
Ejercicio 1: Reescribe el programa de cálculo del salario, con tarifa-ymedia
para las horas extras, y crea una función llamada calculo_salario
que reciba dos parámetros (horas y tarifa).
"""

# def calculo_salario(horas, tarifa):
#     if horas > 40:
#         normal = horas * tarifa
#         extra = (horas - 40) * (tarifa * 0.5)
#         output = normal + extra
#         return output
#     else:
#         output = horas * tarifa
#         return output


# print(calculo_salario(45, 10.50))

"""
Ejercicio 2: Reescribe el programa de calificaciones del capítulo anterior
usando una función llamada calcula_calificacion, que reciba una
puntuación como parámetro y devuelva una calificación como cadena.
"""

# def calcula_calificacion(score):
#     try:
#         calif = float(score)
#     except:
#         print('error')
#         exit()
#     if calif >= 0.9 :
#         print('A')
#     elif calif >= 0.8 :
#         print('B')
#     elif calif >= 0.7 :
#         print('C')
#     elif calif >= 0.6 :
#         print('D')
#     elif calif < 0.6 :
#         print('F')

# calcula_calificacion('s')