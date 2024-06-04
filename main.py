import numpy as np # type: ignore
class Persona():
	__nombre:str
	__edad:int
	__dni:int
	__sexo:str
	def __init__(self,nombre,edad,dni,sexo):
		self.__nombre = nombre
		self.__edad = edad
		self.__dni = dni
		self.__sexo = sexo
	def getNombre(self):
		return self.__nombre
	def getEdad(self):
		return self.__edad
	def getDni(self):
		return self.__dni
	def getSexo(self):
		return self.__sexo
	def mostrar(self) :
		print ('Su nombre es:{}\n su edad es: {}\n su dni es:{}\n su sexo es:{}'.format(self.__nombre,self.__edad,self.__dni,self.__sexo))
	def _str_(self) -> str:
		pass


class gestor():
	__arreglo:list
	def __init__(self,arreglo):
		self.__arreglo = arreglo
	#documentacion de append y explicacion
	def agregarPersona(self):
		nombre =input("ingrese nombre de la persona\n")
		edad =input("ingrese edad de la persona\n")
		dni=input("ingrese dni de la persona\n")
		sexo =input("ingrese sexo de la persona\n")
		nuevaPersona = Persona(nombre,edad,dni,sexo)
		self.__arreglo = np.append(self.__arreglo,nuevaPersona)
	def mostrar(self):
		print(self.__arreglo)
		for i in self.__arreglo:
			print(i.mostrar())
	#documentacion del sort y explicacion
	def ordenarPersonas(self):
		arregloOrdenado = np.sort(self.__arreglo)
		return arregloOrdenado
	#documentacion de where y explicacion(chequear si funca)
	def buscarPersona(self):
		nombre = input("ingrese el nombre a buscar de la persona")
		resultado= np.where(persona.getNombre == nombre for persona in self.__arreglo)
		return resultado
	#documentacion de delete y explicacion
	def eliminarPersona(self):
		nom = input("ingrese nombre de persona a eliminar")
		indice = np.where(self.__arreglo == nom)
		self._arreglo = np.delete(self._arreglo,indice)

if __name__ == "__main__":
	arr = np.array([])
	ungestor=gestor(arr)
	ungestor.agregarPersona()
	ungestor.mostrar()