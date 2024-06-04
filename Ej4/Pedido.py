class Pedido:
    __patenteMoto:str
    __id:str
    __comidas:list
    __tiempoEst:int
    __tiempoReal:int
    __precio:float
    def __init__(self,patente,id,comidas,tiempoEst,precio):
        self.__patenteMoto = patente
        self.__id = id
        self.__comidas = comidas
        self.__tiempoEst = tiempoEst
        self.__tiempoReal = 0
        self.__precio = precio
    def getId(self):
        return self.__id
    def setTiempoEntrega(self,tiempo):
        self.__tiempoReal = tiempo
    