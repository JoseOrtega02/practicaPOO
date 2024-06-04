class Puntaje:
    __DNI:int
    __estilo:str
    __valoracion:list
    def __init__(self,DNI,estilo,valoracion):
        self.__DNI = DNI
        self.__estilo = estilo
        self.__valoracion = valoracion
    def getDNI(self):
        return self.__DNI
    def getEstilo(self):
        return self.__estilo
    def getValoracion(self):
        return self.__valoracion