class Federado:
    def __init__(self,ap,nom,dni,edad,club):
        self.__apellido=ap
        self.__nombre=nom
        self.__dni=dni
        self.__edad=edad
        self.__club=club
    def getdni(self):
        return self.__dni
    def getedad(self):
        return self.__edad
    def getap(self):
        return self.__apellido
    def getnom(self):
        return self.__nombre
    def getclub(self):
        return self.__club
