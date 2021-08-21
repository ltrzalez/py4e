# txt = 'hola mundo'
# print(dir(txt))
# # como prueba de que tiene atributos veremos el largo (length)  de la cadena de caracteres.
# print(len(txt))
# # como prueba de que tiene metodos remplazaremos algunos caracteres.
# print(txt.replace("hola", "chau"))


# import math
# x = math
# print(type(math))
# print(type(9))


# inp = input('Piso de europa')
# piso_eua = int(inp) +1
# print(f"Piso de EUA {piso_eua}")

# class Contador:
#     cuenta = 0

#     def contar(self):
#         self.cuenta += 1
#         print(f"ya conte {self.cuenta}")

# instancia = Contador()

# instancia.contar()
# instancia.contar()
# instancia.contar()
# Contador.contar(instancia)





# class Persona:
#     agnos = 0

#     def __init__(self):
#         print("naci")

#     def vivir(self):
#         self.agnos += 1
#         print(f"ya vivi {self.agnos}")

#     def __del__(self):
#         print("he muerto")

# p = Persona()
# p.vivir()
# p.vivir()
# p.vivir()
# p = "Bala Lirica"
# print("la variable p ahora contiene ", p)


class Persona:
    agno = 0
    nombre = ""

    def __init__(self, argvs): 
        self.nombre = argvs
        print(f"nacio {self.nombre}")

    def vivir(self):
        self.agno += 1
        print(f"{self.nombre} vivio {self.agno}")

    

p1 = Persona("Juan") 
p2 = Persona("Maria") 
p1.vivir()
p2.vivir()
p1.vivir()