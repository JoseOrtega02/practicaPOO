class Patinador:
    __apellido:str
    __nombre:str
    __DNI:int
    __edad:int
    __club:str
    def __init__(self,apellido,nombre,DNI,edad,club):
        self.__apellido =apellido
        self.__nombre = nombre
        self.__DNI = DNI
        self.__edad = edad
        self.__club = club
    def getApellido(self):
        return self.__apellido
    def getNombre(self):
        return self.__nombre
    def getDNI(self):
        return self.__DNI
    def getEdad(self):
        return self.__edad
    def getClub(self):
        return self.__club
