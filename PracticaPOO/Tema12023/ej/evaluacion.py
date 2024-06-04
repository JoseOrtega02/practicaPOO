class Ev:
    def __init__(self,dni=0,ep='',ev=[0,0,0]):
        self.__dni=dni
        self.__ep=ep
        self.__ev=ev
    def __eq__(self,otro):
        return self.__ep==otro
    def getdni(self):
        return self.__dni
    def getest(self):
        return self.__ep
    def prom(self):
        a=0
        for i in self.__ev:
            a+=i
        return a/3
    def __gt__(self,otro):
        return self.prom()>otro.prom()
    def getev(self):
        return self.__ev
