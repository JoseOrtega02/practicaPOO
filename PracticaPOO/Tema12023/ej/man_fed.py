from federeado import Federado
import csv
class ManejadorFederados:
    def __init__(self):
        self.__federados=[]
    def cargaf(self):
        with open('C:\\Users\\users\\Documents\\Cristiannika\\SEGUNDO AÑO DE FACULTAD\\Programacion orientada a objetos\\UNIDAD 2\\Practico\\federados.csv') as archi:
            reader=csv.reader(archi,delimiter=';')
            for f in reader:
                fed=Federado(f[0],f[1],f[2],int(f[3]),f[4])
                self.__federados.append(fed)
    def buscared(self,dni):
        i=0
        while i<len(self.__federados) and self.__federados[i].getdni()!=dni:
            i+=1
        if i<len(self.__federados):
            n=self.__federados[i].getedad()
        else:
            n=0
        return n
    def buscarap(self,dni):
        i=0
        while i<len(self.__federados) and self.__federados[i].getdni()!=dni:
            i+=1
        if i<len(self.__federados):
            n=self.__federados[i].getap()
        else:
            n=''
        return n
    def buscarnom(self,dni):
        i=0
        while i<len(self.__federados) and self.__federados[i].getdni()!=dni:
            i+=1
        if i<len(self.__federados):
            n=self.__federados[i].getnom()
        else:
            n=''
        return n
    def buscarclub(self,dni):
        i=0
        while i<len(self.__federados) and self.__federados[i].getdni()!=dni:
            i+=1
        if i<len(self.__federados):
            n=self.__federados[i].getclub()
        else:
            n=''
        return n
