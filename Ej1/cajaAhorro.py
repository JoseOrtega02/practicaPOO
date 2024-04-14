from CUILVO import verifyCUIL
class cajaAhorro:
    nrocuenta: str
    cuil:str
    apellido:str
    nombre:str
    saldo: float
    def __init__(self,nroCuenta,cuil,apellido,nombre,saldo):
        if(verifyCUIL(cuil)):
            self.nrocuenta = nroCuenta
            self.saldo = saldo
            self.apellido = apellido
            self.nombre = nombre
            self.cuil = cuil
        else:
            return print("Error Cuil incorrecto")
    def mostrarDatos(self):
        print("Nombre: {},Apellido: {}, Cuil:{},Saldo:{},NroCuenta:{}".format(self.nombre,self.apellido,self.cuil,self.saldo,self.nrocuenta))
    def extraer(self,importe):
        res = self.saldo - importe
        if res < 0:
            print("saldo negativo extraccion no realizable")
        else:
            self.saldo = res
            print("extraccion realizada correctamente saldo actual:{}",self.saldo)
    def depositar(self,importe):
        if(importe > 0):
            self.saldo = self.saldo + importe
            print("ingreso realizado correctamente,saldo actual: ",self.saldo)
        else:
            print("El importe es un numero negativo:{},Deposito no realizado".format(importe))