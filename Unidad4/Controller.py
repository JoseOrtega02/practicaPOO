import tkinter as tk
from model import SimonModel
from view import View
from classObjectEndocer import ObjectEncoder
from gestorUsuario import GestorJugadores
from pathlib import Path

class SimonController:
    def __init__(self, root):
        self.model = SimonModel()
        self.view = View(root, self)
        self.root = root
        self.gestor_jugadores = GestorJugadores()
        self.timer = None
        self.start_game()
        self.create_menu()

    def handle_click(self, event):
        clicked_button = event.widget
        index = self.view.buttons.index(clicked_button)
        self.model.user_sequence.append(index)
        self.view.flash_button(index)
        if self.model.check_user_input():
            if self.model.user_input_complete():
                self.model.score += 1
                self.root.after(1000, self.next_round)
        else:
            self.view.show_game_over(self.model.score)
            self.model.user.setPuntaje(self.model.score) 
            self.save_score(self.model.user) 
            self.start_game()

    def createUser(self, nom, nivel):
        self.model.setUser(nom, nivel)
        self.model.mostrarU()

    def next_round(self):
        self.model.user_sequence = []
        self.model.add_random_color()
        self.view.flash_sequence(self.model.sequence)
        self.reset_timer()  

    def start_game(self):
        self.model.reset_game()
        self.next_round()

    def setNivel(self,nivel):
        print(f"nivel:{nivel}")
        self.model.setNivel(nivel)
        self.start_game()
    def save_score(self, user):
        encoder = ObjectEncoder()
        file_path = "pysimonpuntajes.json"
        if Path(file_path).exists():
            existing_data = encoder.leerJSONArchivo(file_path)
        else:
            existing_data = {"usuarios": []}
        existing_data["usuarios"].append(user.toJSON())
        encoder.guardarJSONArchivo(existing_data, file_path)

    def create_menu(self):
        menubar = tk.Menu(self.root)
        self.root.config(menu=menubar)
        puntajes_menu = tk.Menu(menubar, tearoff=0)
        menubar.add_cascade(label="Puntajes", menu=puntajes_menu)
        puntajes_menu.add_command(label="Ver puntajes", command=self.ver_puntajes)
        puntajes_menu.add_separator()
        puntajes_menu.add_command(label="Salir", command=self.root.quit)

    def ver_puntajes(self):
        file_path = "pysimonpuntajes.json"
        self.gestor_jugadores.cargar_jugadores(file_path)
        self.view.show_puntajes(self.gestor_jugadores.jugadores)

    def reset_timer(self):
        if self.model.nivel in ['Experto', 'Super Experto']:
            if self.timer is not None:
                self.root.after_cancel(self.timer)
            self.timer = self.root.after(5000, self.timer_expired)

    def timer_expired(self):
        self.view.show_game_over(self.model.score)
        self.model.user.setPuntaje(self.model.score)
        self.save_score(self.model.user)
        self.start_game()

if __name__ == "__main__":
    root = tk.Tk()
    controller = SimonController(root)
    root.mainloop()