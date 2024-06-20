from datetime import datetime

class Usuario:
    def __init__(self, nom):
        self.__nombre = nom
        self.__fecha = datetime.now().strftime("%d-%m-%Y")
        self.__hora = datetime.now().strftime("%H:%M:%S")
        self.__puntaje = 0
        self.__nivel = 'Principiante' 

    def setPuntaje(self, punt):
        self.__puntaje = punt

    def setNivel(self, nivel):
        self.__nivel = nivel

    def __str__(self):
        return f"{self.__nombre},{self.__fecha},{self.__hora},{self.__puntaje},{self.__nivel}"

    def toJSON(self):
        return {
            "nombre": self.__nombre,
            "puntaje": self.__puntaje,
            "fecha": self.__fecha,
            "hora": self.__hora,
            "nivel": self.__nivel  
        }

    def __gt__(self, other):
        return self.__puntaje > other.__puntaje