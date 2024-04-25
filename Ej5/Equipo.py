class Equipo:
    __identificadorEquipo: str
    __nombre:str
    __golesFavor:int
    __golesContra:int
    __diffGoles:int
    __puntos:int
    def __init__(self,id,name,golesF,golesC,difG,puntos):
        self.__identificadorEquipo = id
        self.__nombre = name
        self.__golesFavor = golesF
        self.__golesContra = golesC
        self.__diffGoles = difG
        self.__puntos = puntos
    def mostrarDatos(self):
        print("Datos : Nombre-",self.__nombre)
    def obtenerID(self):
        return self.__identificadorEquipo
    def obtenerNombre(self):
        return self.__nombre
    def obtenerGolesFavor(self):
        return self.__golesFavor
    def obtenerGolesContra(self):
        return self.__golesContra
    def obtenerGolesDiff(self):
        return self.__diffGoles
    def obtenerGolesPuntos(self):
        return self.__puntos
    
    