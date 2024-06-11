from datetime import datetime


class Usuario:
    __nombre:str
    __puntaje:int
    __fecha:str
    __hora:str
    def __init__(self,nom):
        self.__nombre = nom
        self.__fecha = datetime.now().strftime("%d-%m-%Y")
        self.__hora = datetime.now().strftime("%H:%M:%S")
        self.__puntaje = 0
    def setPuntaje(self,punt):
        self.__puntaje = punt
    def __str__(self):
        return f"{self.__nombre},{self.__fecha},{self.__hora},{self.__puntaje}"