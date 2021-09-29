"""
Ejercicio : El Juego del Gato

* Se desea hacer un juego para niños de gatos.
* Como primer paso se necesita implementar la clase Gato que va a tener 2 atributos: nombre y energía
* En el atributo nombre se va a guardar el nombre del gato
* En el atributo energia se va a guardar cuantas unidades de energia tiene el Gato, los gatos se 
  crean con 0 unidades de energía

El gato puede tener los siguientes comportamientos (se supone en los ejemplos que el gato se llama "Tom")
    
1) Saltar
 - El comportamiento saltar consume 3 unidades de energia 
   - Si al gato le alcanza la energía para saltar debe imprimir:
     "Soy Tom, salte y gaste 3 unidades". Y debe restar esa energía de la que tenía.
   - Si no le alcanza la energía debe imprimir: 
     "Soy Tom, no tengo energia para saltar"  
     
2) Correr
  - Para correr, al gato se le debe decir cuantos minutos va a correr. Cada minuto que corre consume una unidad de energía.
  - Si el gato puede correr esa cantidad de minutos según la cantidad de energía que le queda debe imprimir:
     "Soy Tom, corri 5 minutos". Y luego debe restarse dicha energía a lo que le quedaba disponible
  - Si al gato no le alcanza la energía para correr los minutos que se le pide debe imprimir:
     "Soy Tom, no tengo suficiente energia para correr 8 minutos"
     
3) Comer     
  - Comer se usa para recargar la energía del gato y se le debe indicar cuantas unidades comer
  - Como máximo el gato puede tener 10 unidades de energia que equivalen a 10 unidades de comida
  - Si el gato puede comer la cantidad de unidades que se le indican debe imprimir:
     "Soy Tom, comi 10 unidades"
  - Si el gato no puede comer la cantidad de unidades dado que se va a pasar de las 10 unidades de energia 
    máxima debe imprimir:
     "Soy Tom, no puedo comer mas de: 4 unidades" (suponiendo que tenia 6 unidades de energia)
     
4) Obtener saltos que puede dar
  - Este comportamiento le debe indicar al que lo llama cuantos saltos podría dar el gato según la energía
    que le queda. Por ejemplo si le quedan 6 unidades de energía al llamar a este comportamiento debería devolver:
     2 dado que puede saltar 2 veces dado que cada salto consume 3 unidades
     
5) Obtener informacion del gato
  - Este comportamiento debe imprimir el nombre del gato y cuanta energía le queda, por ejemplo:
     "Soy Tom, me quedan 5 unidades de energia"

** Implementación **

La funcion main() que arranca el juego ya se encuentra implementada y en la cual no hay que cambiar 
nada. 
El objetivo es armar los cuerpos de los metodos en la clase gato para que el juego funcione

""" 



class Gato:

    energia = 0
    nombre = ""

    def set_nombre(self, name):
       self.nombre = name 
    
    def getNombre(self):
      return self.nombre    

    def getEnergia(self):
      return self.energia       

    # def correr(self, tiempo):        

    def saltar(self):
      if self.getEnergia() >= 3:
        self.energia = self.energia - 3
        print('Soy', self.getNombre(), ', salte y gaste 3 unidades')        

    # def mostrarInformacion(self):        

    def comer(self,comida):
      self.energia = comida        

    # def obtenerSaltosQuePuedeDar(self):
        


def main():
    print("El juego del Gato")
    nombre = input("Ingrese el nombre del gato \n")
    gato = Gato()
    gato.set_nombre(nombre)

    operacion = int(input("Elegir opcion (1. Correr, 2.Saltar, 3. Comer, 4.Salir)"))
    

    while operacion >= 1 and operacion <= 3:
        if operacion == 1:
            tiempo_a_correr = input("Ingrese el tiempo en minutos")
            gato.correr(int(tiempo_a_correr))
            pass
        elif operacion == 2:
            gato.saltar()
            pass
        elif operacion == 3:
            cantidad_de_comida = input("ingrese la cantidad de unidades")
            gato.comer(cantidad_de_comida)
            pass
        operacion = int(input("Elegir opcion (1. Correr, 2.Saltar, 3. Comer, 4.Salir)"))
    
    gato.mostrarInformacion()
    print(gato.getNombre() + " puede dar " + str(gato.obtenerSaltosQuePuedeDar()) + " saltos")

main()