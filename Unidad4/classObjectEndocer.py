import json
from pathlib import Path

class ObjectEncoder:
    def decodificarDiccionario(self, d):
        if '__class__' not in d:
            return d
        else:
            class_name = d['__class__']
            class_ = eval(class_name)
        if class_name == 'Manejador':
            usuarios = d['usuarios']
            dPunto = usuarios[0]
            manejador = class_()
        for i in range(len(usuarios)):
            dUsuario = usuarios[i]
            class_name = dUsuario.pop('__class__')
            class_ = eval(class_name)
            atributos = dUsuario['__atributos__']
            unUsuario = class_(**atributos)
            manejador.agregarUsuario(unUsuario)
        return manejador

    def guardarJSONArchivo(self, diccionario, archivo):
        with Path(archivo).open("w", encoding="UTF-8") as destino:
            json.dump(diccionario, destino, indent=4)

    def leerJSONArchivo(self, archivo):
        with Path(archivo).open(encoding="UTF-8") as fuente:
            diccionario = json.load(fuente)
        return diccionario

    def convertirTextoADiccionario(self, texto):
        return json.loads(texto)
