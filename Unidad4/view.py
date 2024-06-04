import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
class View:
    __root:object
    __conrroller:object
    __colores:list
    __buttons:list
    def __init__(self,root,controller):
        self.__root = root
        self.__conrroller = controller
        self.__root.title("Simon Game")
        self.__colores = ["#ff0000","#00ff00","#0000ff","#ffff00"]
        self.__buttons =[]
        self.create_buttons()
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