import numpy as np
from menu import Menu
def main():
    a = np.zeros((5,7))
    menu = Menu(a)
    menu.showMenu()
if __name__ == "__main__":
    main()