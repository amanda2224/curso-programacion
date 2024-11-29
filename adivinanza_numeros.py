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
        print("\n¡El juego ha comenzado!")
        while True:
            try:
                numero = int(input("Adivina el número (entre 1 y 100): "))
                resultado = self.validarNumero(numero)
                print(resultado)
                if resultado == "¡Correcto!":
                    self.jugador.registrarPartida(self.intentos, True)
                    break
            except ValueError:
                print("Por favor, ingresa un número válido.")
        self.guardarEstadisticas()

    def validarNumero(self, numero):
        self.intentos += 1
        if numero > self.numero_secreto:
            return "El número es menor."
        elif numero < self.numero_secreto:
            return "El número es mayor."
        else:
            return "¡Correcto!"

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
        self.historial.append({"intentos": intentos, "gano": gano})

    def mostrarEstadisticas(self):
        partidas_jugadas = len(self.historial)
        partidas_ganadas = sum(1 for partida in self.historial if partida["gano"])
        porcentaje_aciertos = (partidas_ganadas / partidas_jugadas * 100) if partidas_jugadas > 0 else 0
        print(f"\n--- Estadísticas de {self.nombre} ---")
        print(f"Partidas jugadas: {partidas_jugadas}")
        print(f"Partidas ganadas: {partidas_ganadas}")
        print(f"Porcentaje de aciertos: {porcentaje_aciertos:.2f}%")

    def guardarEstadisticas(self):
        with open(f"{self.nombre}_estadisticas.txt", "w") as archivo:
            for partida in self.historial:
                archivo.write(f"{partida['intentos']},{partida['gano']}\n")

    def cargarEstadisticas(self):
        if os.path.exists(f"{self.nombre}_estadisticas.txt"):
            with open(f"{self.nombre}_estadisticas.txt", "r") as archivo:
                for linea in archivo:
                    intentos, gano = linea.strip().split(",")
                    self.historial.append({"intentos": int(intentos), "gano": gano == "True"})


# Función principal para ejecutar el programa
def menu():
    print("¡Bienvenido al Juego de Adivinanza de Números!")
    nombre = input("¿Cómo te llamas? ").capitalize()
    juego = JuegoAdivinanza(nombre)
    juego.cargarEstadisticas()

    while True:
        print("\n--- Menú Principal ---")
        print("1. Jugar una nueva partida")
        print("2. Ver estadísticas")
        print("3. Salir")
        opcion = input("Elige una opción: ")

        if opcion == "1":
            juego.iniciarJuego()
        elif opcion == "2":
            juego.mostrarEstadisticas()
        elif opcion == "3":
            print("Gracias por jugar. ¡Hasta pronto!")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")


# Iniciar el programa
if __name__ == "__main__":
    menu()
