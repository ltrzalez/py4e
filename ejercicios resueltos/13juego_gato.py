class Gato:

    energia = 0
    nombre = ""

    def set_nombre(self, name):
        self.nombre = name
    
    def getNombre(self):
        return self.nombre

    def getEnergia(self):
        return self.energia

    def correr(self, tiempo):
        if self.getEnergia() < tiempo:
            print("Soy " + self.getNombre() + ", no tengo energia " + str(tiempo) + " minutos")
        else:
            print("Soy " + self.getNombre() + ", corri", str(tiempo) + " minutos")
            self.energia -= tiempo

    def saltar(self):
        if self.getEnergia() >= 3:
            print("Soy " + self.getNombre() + ", salte y gaste 3 unidades")
            self.energia -= 3
        else:
            print("Soy " + self.getNombre() + ", no tengo energia para saltar")

    def mostrarInformacion(self):
        print("Soy " + self.getNombre() + ", me quedan " + str(self.getEnergia()) + " unidades de energia")

    def comer(self,comida):
        if(int(comida) + self.getEnergia() > 10 or comida == 0):
            maximoPosibleDeComida = 10 - self.getEnergia()
            print("Soy " + self.getNombre() + ", no puedo comer mas de: " + str(maximoPosibleDeComida) + " unidades")
        else:
            self.energia += int(comida)
            print("Soy " + self.getNombre() + ", comi " + str(comida) + " unidades")

    def obtenerSaltosQuePuedeDar(self):
        return self.getEnergia() // 3


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