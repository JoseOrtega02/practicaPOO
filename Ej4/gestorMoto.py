import csv
class gestorMoto():
    __datosMotos:list
    def __init__(self):
        with open("datosMotos.csv","r",newline="") as csvFile:
            self.__datosMotos = csv.DictReader(csvFile)
            print("Datos cargados")
    def validarExistencia(self,patente):
        res = False
        for moto in self.__datosMotos:
            if(moto.getPatente() == patente):
                res = True
        return res