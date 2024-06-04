def comidas():
    comidas = []
    comida = input("ingrese comida(0 para terminar)")
    while comida != "0":
        comidas.append(comida)
        comida = input("ingrese comida(0 para terminar)")
    return comidas