import tkinter as tk
from tkinter import StringVar, Toplevel, ttk
from tkinter import messagebox
class View:
    __root:object
    __conrroller:object
    __colores:list
    __buttons:list
    __dialogo:object
    __nomU:str
    def __init__(self,root,controller):
        self.__root = root
        self.__conrroller = controller
        self.__root.title("Simon Game")
        self.nombre()
        self.__colores = ["#ff0000","#00ff00","#0000ff","#ffff00"]
        self.__buttons =[]
        self.create_buttons()
    def nombre(self):
        self.__dialogo = tk.Toplevel()
        self.__dialogo.geometry("500x500")
        self.__dialogo.title("nombre")
       
        
        etiq = ttk.Label(self.__dialogo,text="Jugador")
        self.__nomU= StringVar()
        self.__nomU.set("") 
        input=ttk.Entry(self.__dialogo,textvariable=self.__nomU,width=30)

        etiq.pack(side="left")
        input.pack(side="right")
        boton = ttk.Button(self.__dialogo, text='Cerrar',command=self.handleBtnUser)
        boton.pack(side="bottom", padx=20, pady=20)

        self.__root.wait_window(self.__dialogo)
    
    def handleBtnUser(self):
        self.__conrroller.createUser(self.__nomU.get())
        self.__dialogo.destroy()
    @property
    def buttons(self):
        return self.__buttons
    def create_buttons(self):
        for i,color in enumerate(self.__colores):
            canvas= tk.Canvas(self.__root,bg=color,width=200,height=200)
            canvas.grid(row=i//2,column=i%2,padx=10,pady=10)
            canvas.bind("<Button-1>",self.__conrroller.handle_click)
            self.__buttons.append(canvas)
    def flash_button(self,index):
        button= self.__buttons[index]
        original_color= button["bg"]
        button["bg"]= "white"
        button.update_idletasks()
        self.__root.after(500,lambda:button.config(bg=original_color))
    def flash_sequence(self,sequence):
        for i,index in enumerate(sequence):
            self.__root.after(i*1000,lambda index=index:self.flash_button(index))
    def show_game_over(self,score):
        messagebox.showinfo("GAME OVER",f"Puntaje:{score}")
if __name__ == "__main__":
    view= View()
    view.mainloop()