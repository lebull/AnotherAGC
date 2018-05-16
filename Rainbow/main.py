#Tetris Psudo
import sys
import time
import random

from screen import Screen, ScreenColors

screen = Screen((10, 20))

LINE = 1                #def
NUM_LINE = 4            #def
LINE_SHAPES = [
#   |.   .   .   .   |
    "    XXXX        ",
    "  X   X   X   X ",
    "        XXXX    ",
    " X   X   X   X  "
]

SQUARE = "square"       #def
NUM_SQUARE = 1          #def
SQUARE_SHAPES = [
    "     XX  XX     "
]

ELL = "ell"             #def

blocks = {
    "ell": [],
    "bell": [],
    "tee": [],
    "zig": [],
    "zag": []
}

def blitBlock(shape, orientation, pos, unblit):

    #case
    if(shape == LINE):
        shapeData = LINE_SHAPES[orientation]

    i = 0
    while i < 16:
        targetPos = (pos[0] + i/4, pos[1] + i%4)
        if(shapeData[i] == "X"):
            if(unblit):
                color = ScreenColors.BG_DEFAULT
            else:
                color = ScreenColors.BG_RED
            #should be handled by its own opcode
            setScreenColor((targetPos[1], targetPos[0]), color)
        i+=1

def setScreenColor(pos, color):
    screen.data[pos[0]][pos[1]] = color

#16 bit var
currentShape = {
    "shape": LINE, #3
    "orientation": 0,     #2
    "pos": (0, 0)         #5, 6
}

#Rotates the currentShape if allowed.  Does nothing otherwise.
def rotate(direction):
    global currentShape
    if(currentShape["shape"] == LINE):
        pass

#Return a 4x4 grid of occupied spots on the board, encoded
# as 16 bits.  OOBs will be considered "occupied".
def getQuartFromBoard(pos):
    pass

#Returns true if any two corrisponding spots of two quarts are both occupied.
#At lower levels, this should be the same as a series of ANDS
def doesConflict(quart1, quart2):
    pass


#Main execution
for i in range(8):
    currentShape["orientation"] = i % NUM_LINE
    currentShape["pos"] = (currentShape["pos"][0], currentShape["pos"][1] + 1)

    blitBlock(
        currentShape["shape"],
        currentShape["orientation"],
        currentShape["pos"],
        False)
    screen.printout()

    time.sleep(0.5)

    blitBlock(
        currentShape["shape"],
        currentShape["orientation"],
        currentShape["pos"],
        True)
