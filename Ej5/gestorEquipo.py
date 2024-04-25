from Equipo import Equipo
import csv
class gestorEquipo:
    def ingresarEquipo(self,equipo:Equipo):
        print(equipo)
        
        with open("equipo2024.csv","w",newline="") as csvfile:
            campos = ["id","nombre","GolesFavor","GolesContra","DiffGoles","Puntos"]
            equipoWriter = csv.DictWriter(csvfile,fieldnames=campos)
            equipoWriter.writeheader()
            equipoWriter.writerow({"id":equipo.obtenerID(),"nombre":equipo.obtenerNombre(),"GolesFavor":equipo.obtenerGolesFavor(),"GolesContra":equipo.obtenerGolesContra(),"DiffGoles":equipo.obtenerGolesDiff(),"Puntos":equipo.obtenerGolesPuntos()})
    def mostrarEquipo(self):
        with open("equipo2024.csv","r",newline="") as csvfile:
            equipoReader = csv.DictReader(csvfile)
            print("Datos equipo: ")
            for fila in equipoReader:
                print(fila)

