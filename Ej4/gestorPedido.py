import csv
from Pedido import Pedido
class gestorPedido:
    __datosPedido:list
    def __init__(self):
        with open("datosPedidos.csv","r",newline="") as csvFile:
            self.__datosPedido = csv.DictReader(csvFile)
            print("datos cargados")
    def crearPedido(self,patente,id,comidas,tiempoEst,precio):
        nuevoPedido = Pedido(patente,id,comidas,tiempoEst,precio)
        self.__datosPedido.append(nuevoPedido)
    def entrega(self,id,tiempo):
        for pedido in self.__datosPedido:
            if(pedido.getId() == id):
                pedido.setTiempoEntrega(tiempo)
            