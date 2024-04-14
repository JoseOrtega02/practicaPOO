def verifyCUIL(cuil:str):
    listaCuil = list(cuil)
    X = listaCuil[0]
    Y = listaCuil[1]
    Z = listaCuil[-1]
    medio =listaCuil[0:-1]
    multiplicadores = [5,4,3,2,7,6,5,4,3,2]
    suma = 0
    XY= X+Y
    if(XY != "20" and XY !="27" and XY != "30"):
        return False
    for i in range(len(medio)):
        suma +=int(medio[i]) * multiplicadores[i]
    resto = suma % 11
    if(resto == 0):
        Z=0
    if(resto == 1):
        if(XY == 20):
            Z= 9
        if(XY == 27):
            Z = 4
        else:
            Z = 11 - resto
    verificacion = str( XY + "".join(map(str,listaCuil[2:-1])) + Z)
    if(verificacion == cuil):
        return True
    else:
        return False
        
