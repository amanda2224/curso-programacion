import random
import os

# Clase madre que conttrola todo el juegp
class JuegoAdivinanza:
    def __init__(self, nombreJugador):
        self.jugador = Jugador(nombreJugador)
        self.numero_secreto = None
        self.intentos = 0

    def iniciarJuego(self):
        self.reiniciarJuego()
        print("El juego ha empezadoo!")
        while True:
            try:
                numero = int(input("Adivina el número (entre 1 y 100): "))
                resultado = self.validarNumero(numero)
                print(resultado)
                if resultado == "has logrado encontrar el numero!":
                    self.jugador.registrarPartida(self.intentos, True)
                    break
            except ValueError:
                print("debes de ingresar un numero valido entre 1 y 100")
        self.guardarEstadisticas()

    def validarNumero(self, numero):
        self.intentos += 1
        if numero > self.numero_secreto:
            return "El número es menor ."
        elif numero < self.numero_secreto:
            return "El número es mayor."
        else:
            return "has logrado encontrar el numero!"

    def reiniciarJuego(self):
        self.numero_secreto = random.randint(1, 100)
        self.intentos = 0

    def mostrarEstadisticas(self):
        self.jugador.mostrarEstadisticas()

    def guardarEstadisticas(self):
        self.jugador.guardarEstadisticas()

    def cargarEstadisticas(self):
        self.jugador.cargarEstadisticas()


# Clase que administra la información del jugador
class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        self.historial = []

    def registrarPartida(self, intentos, gano):
        self.historial.append({"intentos": intentos, "ganaste :)": gano})

    def mostrarEstadisticas(self):
        partidas_jugadas = len(self.historial)
        partidas_ganadas = sum(1 for partida in self.historial if partida["ganaste :)"])
        porcentaje_aciertos = (partidas_ganadas / partidas_jugadas * 100) if partidas_jugadas > 0 else 0
        print(f"\n--- Estadísticas de {self.nombre} ---")
        print(f"Partidas jugadas: {partidas_jugadas}")
        print(f"Partidas ganadas: {partidas_ganadas}")
        print(f"Porcentaje de aciertos: {porcentaje_aciertos:.2f}%")

    def guardarEstadisticas(self):
        with open(f"{self.nombre}_estadisticas.txt", "w") as archivo:
            for partida in self.historial:
                archivo.write(f"{partida['intentos']},{partida['ganaste :)']}\n")

    def cargarEstadisticas(self):
        if os.path.exists(f"{self.nombre}_estadisticas.txt"):
            with open(f"{self.nombre}_estadisticas.txt", "r") as archivo:
                for linea in archivo:
                    intentos, gano = linea.strip().split(",")
                    self.historial.append({"intentos": int(intentos), "ganaste :)": gano == "True"})


#menu para el programa 
def menu():
    print(" hola :) bienvenido al juego de adivinanza el numero")
    nombre = input("nombre del jugador: ").capitalize()
    juego = JuegoAdivinanza(nombre)
    juego.cargarEstadisticas()

    while True:
        print("--- menu ---")
        print("1. jugar una partida nueva")
        print("2. veer estadísticas")
        print("3. Salir")
        opcion = input("elija una opción: ")

        if opcion == "1":
            juego.iniciarJuego()
        elif opcion == "2":
            juego.mostrarEstadisticas()
        elif opcion == "3":
            print("nos vemos :)")
            break
        else:
            print("opción no válida")


# Iniciar el programa
if __name__ == "__main__":
    menu()
