import random
from usuarioClass import Usuario

class SimonModel:
    def __init__(self):
        self.sequence = []
        self.user_sequence = []
        self.score = 0
        self.user = None
        self.nivel = 'Principiante'

    def setUser(self, nom, nivel):
        self.user = Usuario(nom)
        self.nivel = nivel
        self.user.setNivel(nivel)
    def setNivel(self,nivel):
        self.nivel = nivel
    def mostrarU(self):
        print(f"{self.user}")

    def reset_game(self):
        self.sequence = []
        self.user_sequence = []
        self.score = 0

    def add_random_color(self):
        if self.nivel == "Principiante" or self.nivel =="Experto":
            self.sequence.append(random.randint(0, 3))
        elif self.nivel == 'Super Experto':
            self.sequence.append(random.randint(0, 3))
            self.sequence.append(random.randint(0, 3))

    def check_user_input(self):
        return self.user_sequence == self.sequence[:len(self.user_sequence)]

    def user_input_complete(self):
        return len(self.user_sequence) == len(self.sequence)