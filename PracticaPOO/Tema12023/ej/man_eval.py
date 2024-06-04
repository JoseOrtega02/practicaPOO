from evaluacion import Ev
from man_fed import ManejadorFederados
import csv
class ManejadorEvaluaciones:
    def __init__(self):
        self.__evaluaciones=[]
    def cargaev(self):
        with open('C:\\Users\\users\\Documents\\Cristiannika\\SEGUNDO AÑO DE FACULTAD\\Programacion orientada a objetos\\UNIDAD 2\\Practico\\evaluacion.csv') as archi:
            reader=csv.reader(archi,delimiter=';')
            for f in reader:
                e=Ev(f[0],f[1],[float(f[2]),float(f[3]),float(f[4])])
                self.__evaluaciones.append(e)
    def busc(self,estilo,edad,mf=ManejadorFederados()):
        i=0
        print(f'Estilo de presentacion:{estilo}\tEdad:{edad}\n')
        for ev in self.__evaluaciones:
            if ev==estilo:
               d=mf.buscared(ev.getdni())
               if d!=0 and d==edad:
                   print(f'{mf.buscarap(ev.getdni())},{mf.buscarnom(ev.getdni())},{ev.getdni()}\n')
    def may(self,mf=ManejadorFederados()):
        aux=Ev()
        for ev in self.__evaluaciones:
            if ev>aux:
                aux=ev
        print(f'El patinador con mayor puntaje es:{mf.buscarap(aux.getdni())} {mf.buscarnom(aux.getdni())} {aux.getest()} {mf.buscarclub(aux.getdni())}\n')
    def buscaest(self,mf=ManejadorFederados()):
        print('Patinadores que fueron evaluados en ambos estilos:\n')
        l=[]
        for ev in self.__evaluaciones:
            dni=ev.getdni()
            x=0
            for j in self.__evaluaciones:
                if j.getdni()==dni:
                    x+=1
            if x>1:
                if len(l)==0:
                    l.append(ev)
                else:
                    i=0
                    while i<len(l) and l[i].getdni()!=ev.getdni():
                        i+=1
                    if i>len(l):
                        l.append(ev)
        for e in l:
            print(f'{mf.buscarap(e.getdni())} {mf.buscarnom(e.getdni())}, {e.getdni()}, {mf.buscarclub(e.getdni())}\n')
    def puntaje(self,dni,est):
        i=0
        while i<len(self.__evaluaciones) and (self.__evaluaciones[i].getdni()!=dni and self.__evaluaciones[i].getest()!=est):
            i+=1
        if i<len(self.__evaluaciones):
            print(f'Puntajes:{self.__evaluaciones[i].getev()}')