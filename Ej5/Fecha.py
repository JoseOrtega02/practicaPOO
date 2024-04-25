class Fecha:
     __fecha: str
     __idlocal: str
     __idvisitante:str
     __cantGolLocal:int
     __cantGolVisitante:int
     def __init__(self,fecha,idlocal,idvisit,cantGolLocal,cantGolvisit):
          self.__fecha = fecha
          self.__idlocal = idlocal
          self.__idvisitante = idvisit
          self.__cantGolLocal = cantGolLocal
          self.__cantGolVisitante = cantGolvisit