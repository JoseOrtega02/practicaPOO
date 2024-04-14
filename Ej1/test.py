from cajaAhorro import cajaAhorro
def crearCaja(i):
    nombre = input("Ingrese su nombre: ")
    apellido= input("ingrese su apellido: ")  
    cuil=input("ingrese su CUIL(sin separaciones): ")
    nro =i+ 1
    saldo= 0
    cuenta = cajaAhorro(nro,cuil,apellido,nombre,saldo)
    return cuenta
def test():
    listaCuentas = []
    for i in range(3):
        listaCuentas.append(crearCaja(i))
    for i in range(len(listaCuentas)):
        listaCuentas[i].mostrarDatos()
test()