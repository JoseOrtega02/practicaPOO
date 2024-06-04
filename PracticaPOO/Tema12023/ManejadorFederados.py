class ManejadorFederados:
    __federados:list
    def __init__(self):
        with open("federados.csv","r",newline="") as csvFile:
            self.__federados = [csvFile]
        print(self.__federados)
    def buscarFed(self,lista,edad):
        list = []
        for i in lista:
            j = 0
            while j < len(self.__federados):
                if i.getEdad() == self.__federados[j].getEdad():
                    list += self.__federados[j]
                j = j+1
        return list
       