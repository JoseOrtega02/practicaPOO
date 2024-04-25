import numpy as np
from dias import dias
class Menu:
    __options:dict
    __optionsList:list
    __arreglo:list
    def __init__(self,arreglo):
        self.__options = dict(a=self.optionA,b=self.optionB,c=self.optionC,d=self.optionD,e=self.optionE)
        self.__optionsList = ["a","b","c","d","e"]
        self.__arreglo = arreglo
    def optionA(self):
        dia = input("ingrese dia de la semana")
        sucursal = input("ingrese el codigo de la sucursal")
        importe= input("ingrese el importe")
        diaNum = dias(dia.lower())
        self.__arreglo[int(sucursal)-1,diaNum] = float(importe)
        print(self.__arreglo)
        self.showMenu()
    def optionB(self):
        sucursal=input("ingrese el codigo de sucursal: ")
        suma=0
        for i in self.__arreglo[int(sucursal)-1,:]:
            suma = suma + i
        print("total de facturacion de la sucursal:",suma)
        self.showMenu()
    def optionC(self):
        columna = dias(input("ingrese el dia de la semana"))
        sucursal = np.argmax(self.__arreglo[:,columna])
        print("sucursal que mas gana en ese dia d ela semana: ",sucursal+1)
        self.showMenu()
    def optionD(self):
        codigo= np.argmin(np.argmin(self.__arreglo,axis=1))
        print("codigo del menor importe en la semana: ",codigo+1)
        self.showMenu()
    def optionE(self):
        suma =0
        for i in self.__arreglo:
            for j in i:
                suma = suma + j
        print(suma)
        self.showMenu()
    def showMenu(self):
        for string in self.__optionsList:
            print(string)
        optionSelected = input("Ingrese una opcion por teclado: ")
        self.__options[optionSelected]()