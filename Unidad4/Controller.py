from model import SimonModel
from view import View
import tkinter as tk
class SimonController:
    def __init__(self,root):
        self.model= SimonModel()
        self.view = View(root,self)
        self.root = root
        self.start_game()
    def handle_click(self,event):
        clicked_button = event.widget
        index = self.view.buttons.index(clicked_button)
        self.model.user_sequence.append(index)
        self.view.flash_button(index)
        if self.model.check_user_input():
            if self.model.user_input_complete():
                self.model.score +=1
                self.root.after(1000,self.next_round)
        else:
            self.view.show_game_over(self.model.score)
            self.start_game()
    def next_round(self):
        self.model.user_sequence=[]
        self.model.add_random_color()
        self.view.flash_sequence(self.model.sequence)
    def start_game(self):
        self.model.reset_game()
        self.next_round()
if __name__ == "__main__":
    root = tk.Tk()
    controller = SimonController(root)
    root.mainloop()