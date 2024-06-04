from gestorMoto import gestorMoto
from gestorPedido import gestorPedido
import comidas as comidas
class Menu:
    __gestorMotos: gestorMoto
    __gestorPedidos: gestorPedido
    def __init__(self):
        self.__gestorMotos = gestorMoto()
        self.__gestorPedidos = gestorPedido()
    def cargarPedidos(self):
        moto = input("ingresar patente de la moto asignada")
        validacion =self.__gestorMotos.validarExistencia(moto)
        if(validacion):
            id = input("Ingrese iddentificador del pedido")
            comidasArr = comidas()
            tiempoEst = input("Ingrese tiempo estimado del pedido")
            precio = input("ingrese precio del  pedido")
            self.__gestorPedidos.crearPedido(moto,id,comidasArr,tiempoEst,precio)
            print("pedido creado")
        else:
            print("la moto no existe")
        self.showMenu()
    def entregarPedido(self):
        patente = input("ingrese patente")
        validacion = self.__gestorMotos.validarExistencia(patente)
        if(validacion):
            idPedido = input("ingrese identificador del pedido")
            tiempoEntrega = input("ingrese el tiempo de entrega en minutos")
            self.__gestorPedidos.entrega(idPedido,tiempoEntrega)
            print("tiempo de entrega actualizado")
        else:
            print("la moto no existe")
        self.showMenu()
    