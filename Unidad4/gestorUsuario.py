import json
from pathlib import Path
from usuarioClass import Usuario

class GestorJugadores:
    def __init__(self):
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def cargar_jugadores(self, archivo):
        if Path(archivo).exists():
            with open(archivo, 'r', encoding='utf-8') as f:
                data = json.load(f)
                for item in data["usuarios"]:
                    jugador = Usuario(item["nombre"])
                    jugador.setPuntaje(item["puntaje"])
                    jugador._Usuario__fecha = item["fecha"]  # Accessing the private attribute directly
                    jugador._Usuario__hora = item["hora"]    # Accessing the private attribute directly
                    self.agregar_jugador(jugador)
            self.jugadores.sort(reverse=True)

    def mostrar_puntajes(self):
        for jugador in self.jugadores:
            print(jugador)

    def toJSON(self):
        return {
            "usuarios": [jugador.toJSON() for jugador in self.jugadores]
        }
