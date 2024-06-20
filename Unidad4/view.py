import tkinter as tk
from tkinter import StringVar, Toplevel, ttk, messagebox

class View:
    def __init__(self, root, controller):
        self.root = root
        self.controller = controller
        self.root.title("Simon Game")
        self.nombre()
        self.colores = ["#ff0000", "#00ff00", "#0000ff", "#ffff00"]
        self.buttons = []
        self.create_buttons()

    def nombre(self):
        self.dialogo = Toplevel()
        self.dialogo.title("Usuario")
        etiq = ttk.Label(self.dialogo, text="Jugador")
        self.nomU = StringVar()
        self.nomU.set("")
        input = ttk.Entry(self.dialogo, textvariable=self.nomU, width=30)
        etiq.pack(side="left")
        input.pack(side="right")
        boton = ttk.Button(self.dialogo, text='Iniciar Juego', command=self.handleBtnUser)
        boton.pack(side="bottom", padx=20, pady=20)

    def handleBtnUser(self):
        self.controller.createUser(self.nomU.get())
        self.dialogo.destroy()

    def create_buttons(self):
        for i, color in enumerate(self.colores):
            canvas = tk.Canvas(self.root, bg=color, width=200, height=200)
            canvas.grid(row=i // 2, column=i % 2, padx=10, pady=10)
            canvas.bind("<Button-1>", self.controller.handle_click)
            self.buttons.append(canvas)

    def flash_button(self, index):
        button = self.buttons[index]
        original_color = button["bg"]
        button["bg"] = "white"
        button.update_idletasks()
        self.root.after(500, lambda: button.config(bg=original_color))

    def flash_sequence(self, sequence):
        for i, index in enumerate(sequence):
            self.root.after(i * 1000, lambda index=index: self.flash_button(index))

    def show_game_over(self, score):
        messagebox.showinfo("GAME OVER", f"Puntaje: {score}")

    def show_puntajes(self, jugadores):
        dialogo = Toplevel(self.root)
        dialogo.title("Galería de Puntajes")
        tree = ttk.Treeview(dialogo, columns=("Jugador", "Fecha", "Hora", "Puntaje"), show="headings")
        tree.heading("Jugador", text="Jugador")
        tree.heading("Fecha", text="Fecha")
        tree.heading("Hora", text="Hora")
        tree.heading("Puntaje", text="Puntaje")
        for jugador in jugadores:
            tree.insert("", "end", values=(jugador._Usuario__nombre, jugador._Usuario__fecha, jugador._Usuario__hora, jugador._Usuario__puntaje))
        tree.pack(padx=20, pady=20)
        boton = ttk.Button(dialogo, text="Cerrar", command=dialogo.destroy)
        boton.pack(pady=10)
