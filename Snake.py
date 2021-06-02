# at the moment, the game only works in Windows
from random import randint as rand # to generate random "food"
from platform import system as plat # to known the platform
from os import system as sys # to update the screen
from time import time as t # for time between keys
import msvcrt # to detect keys

def key(difficulty): # captures the pressed key
    start = t()
    while(True):
        if(msvcrt.kbhit()):
            entry = msvcrt.getch()
            if(entry == b'H' or entry == b'w' or entry == b'W'):    # UP
                return 1
            elif(entry == b'K' or entry == b'a' or entry == b'A'):    # LEFT
                return 2
            elif(entry == b'P' or entry == b's' or entry == b'S'):    # DOWN
                return 3
            elif(entry == b'M' or entry == b'd' or entry == b"D"):    # RIGHT
                return 4
            elif(entry == b' ' or entry == b'\r'):
                return -1
        elif(t() - start >= (1/difficulty)):
            return 0

def dimensions(board, x = 20,y = 10): # initializes the board with empty posisions
    for row in range(y):
        tablero.append([])
        for column in range(x):
            tablero[row].append(0)

def reset(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j] = 0            
            
def display(board, snake, food): # displays the board
    # the board is a multidimensional attay of integers
    # 0 -> nothing
    # 1 -> head of the snake
    # 2 -> body of the snake
    # 3 -> food

    reset(board)
    
    head = ["▲","◄","▼","►"]

    board[snake[1][0][0]][snake[1][0][1]] = 1

    if(len(snake[1]) > 1):
        for x,y in snake[1][1:]:
            board[x][y] = 2
    
    board[food[0]][food[1]] = 3

    print(" - " * (len(board[0]) + 1))
    for i in range(len(board)):
        print("|",end="")
        for j in range(len(board[0])):
            current = board[i][j]
            if(current == 0):
                print(" "," ", end = "")
            elif(current == 1):
                print(head[snake[0] - 1]," ", end = "")
            elif(current == 2):
                print("o"," ", end = "")
            elif(current == 3):
                print("*"," ", end = "")
        else:
            print("|")
    else:
        print(" - " * (len(board[0]) + 1))            
            
def run(difficulty): # returns total score
    clean_screen = "cls" if(plat() == 'Windows') else "clear" # gets the method to clean screen depending on the platform
    snake = [rand(3,4),[[0,0]]] # initialize the snake in the upper left corner
    # the snake is compound by its direction abd its body
    # the body its compound by the head in the first position and the rest of the body for the following positions (arrays)
    board = [] # main board  
    x, y = 0, 0  # board dimensions
    cont = True # controls the game cycle
    food = False # indicates if there's food in the board
    score = 0

    print("Make sure that the screen you're playing in it's big enough to support the dimensions...")
    while(True):
        try:
            x = int(input("Enter the width of the board: "))
            break
        except:
            print("Try again...\n")

    while(True):
        try:
            y = int(input("Enter the height of the board: "))
            break
        except:
            print("Try again...\n")

    dimensions(board, x, y)

    input("\nGAME READY\nPress ENTER to play\nSPACE or ENTER to exit (while playing)...")
    
    while(cont):
        sys(clean_screen) # cleans the screen

        if(not food): # slice to generate food in the board
            food = [rand(0,y-1), rand(0, x-1)]
            while(food in snake[1]): # verifies that the food has not appeared inside the snake
                food = [rand(0,y-1), rand(0, x-1)]

                if(len(snake[1]) == (x * y)): # if the snake occupies the whole board
                   return [x*y]
            food = True

        display(board,snake,food) # displays the board
        button = key(difficulty) # gets the pressed key
        if(button == -1): # if SPACE / ENTER was pressed
             cont = False
        else:
            next_iter = displacement(board, snake, button, food) # displaces the snake depending off the keyboard entry

            if(cont == 1): # the snake ate
                score += 1
                food = False
            elif(cont == -1): # a collision occured
                cont = False

    return score

def play(): # driver function that returns total score
    difficulty = 0
    msg = "Press ENTER to continue..."
    
    while(True):
        try:
            difficulty = int(input("\nS-N-A-K-E\n\nEnter the difficulty of the game (more than 0): "))
            if(difficulty > 0):
                break
            else:
                print("Try again...\n")
        except:
            print("Try again...\n")
    try:
        score = run(difficulty)

        if(type(score) == list):
            input("CONGRATS!!, YOU FILLED THE BOARD\nGAME OVER\n%s" % msg)
            return score[0]
    except:
        input("GAME INTERRUPTED\Final Score: %d\n%s" % (score, msg))
        return score
    else:
        input("GAME OVER\nFinal score: %d\n%s" % (score, msg))
        return score

if(__name__ == "__main__"): # for main module
    play()
