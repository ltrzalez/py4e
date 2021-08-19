# ejercicios: nombre un metodo que encuentra el mayor numero de una lista
# respuesta max()  print(max([1,5,3,523,86,3]))


# loop para sacar promedio

# unidades, promedio, total = 0, 0, 0
# for value in [3, 41, 12, 9, 74, 15] :
#     total += value
#     unidades += 1
# promedio = total / unidades
# print(promedio, total, unidades)

"""
Ejercicio 1: Escribe un programa que lea repetidamente números hasta
que el usuario introduzca “fin”. Una vez se haya introducido “fin”,
muestra por pantalla el total, la cantidad de números y la media de
esos números. Si el usuario introduce cualquier otra cosa que no sea un
número, detecta su fallo usando try y except, muestra un mensaje de
error y pasa al número siguiente.

"""
# contador, total = 0, 0
# while True:
#     entrada = input('give me a number \n')
#     if entrada == 'fin':
#         break
#     try:
#         entrada = int(entrada)
#     except:
#         print('el dato ingresado no es un numero')
#         continue
#     contador += 1
#     total += entrada

# if contador > 0:
#     promedio = total / contador
#     print(promedio, total, contador)


"""
Ejercicio 2: Escribe otro programa que pida de a un numero, que al recibir "done" termine el programa,
que responda "invalid input" cuando no sea un numero y muestre por pantalla el máximo y mínimo de los
números.

"""

# all_numbers = []
# largest = None
# smallest = None

# while True:
#     num = input("Enter a number: ")
#     if num == "done" : break
#     try:
#         value=int(num)
#         all_numbers.append(value)
#     except:
#         print("Invalid input")


# largest = max(all_numbers)
# smallest = min(all_numbers)    

# print("Maximum is", largest)
# print("Minimum is", smallest)