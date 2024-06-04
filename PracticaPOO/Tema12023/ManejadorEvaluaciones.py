class ManejadorEvaluaciones:
    __Evaluaciones:list
    def __init__(self):
        with open("evaluaciones.csv","r",newline="") as csvFile:
            self.__Evaluaciones = [csvFile]
        print(self.__Evaluaciones) 
    def buscar(self,estilo):
        list = []
        i =0
        while i < len(self.__Evaluaciones):
            if i.getEstilo() == estilo:
                list += i
            i = i+1
        return list