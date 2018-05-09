#Tetris Psudo
import sys
import time
import random

from screen import Screen

screen = Screen((10, 20))

for t in range(10000):
    pos = (random.randint(0, tetris.size[0]-1), random.randint(0, tetris.size[1]-1))
    screen.data[pos[1]][pos[0]] = ScreenColors.random()
screen.printout()

    #time.sleep(0.01)

#sys.stdout.write("\033[41m  \033[0m\n")
raw_input("Enter to continue.")
screen.clear()
