import random
class SimonModel:
    def __init__(self):
        self.sequence= []
        self.user_sequence=[]
        self.score =0
    def reset_game(self):
        self.sequence=[]
        self.user_sequence=[]
        self.score=0
    def add_random_color(self):
        self.sequence.append(random.randint(0,3))
    def check_user_input(self):
        return self.user_sequence == self.sequence[:len(self.user_sequence)]
    def user_input_complete(self):
        return len(self.user_sequence) == len(self.sequence)