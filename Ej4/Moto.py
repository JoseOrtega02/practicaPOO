class Moto():
    __patente:str
    __marca:str
    __NyAConductor:str
    __km:float
    def __init__(self,patente,marca,NyA,Km):
        self.__patente = patente
        self.__marca = marca
        self.__NyAConductor = NyA
        self.__km = Km
    def getPatente(self):
        return self.__patente