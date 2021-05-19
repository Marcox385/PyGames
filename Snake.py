from random import randint as rand # to generate random "food"
from platform import system as plat # to known the platform

def dimensions(board, x = 20,y = 10): # initializes the board with empty posisions
    for row in range(y):
        tablero.append([])
        for column in range(x):
            tablero[row].append(0)

def run(difficulty): # returns total score
    clean_screen = "cls" if(plat() == 'Windows') else "clear" # gets the method to clean screen depending on the platform
    snake = [rand(3,4),[[0,0]]] # initialize the snake in the upper left corner
    # the snake is compound by its direction abd its body
    # the body its compound by the head in the first position and the rest of the body for the following positions (arrays)
    board = [] # main board  
    x, y = 0, 0  # board dimensions
    continue = True # controls the game cycle
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
    
    while(continue):
        sys(clean_screen) # cleans the screen

        if(not food): # slice to generate food in the board
            food = [rand(0,y-1), rand(0, x-1)]
            while(food in snake[1]): # verifies that the food has not appeared inside the snake
                food = [rand(0,y-1), rand(0, x-1)]

                if(len(snake[1]) == (x * y)): # si la serpiente ocupa todo el tablero
                   return [x*y]
            hay_comida = True

        mostrar(tablero,serpiente,comida) # imprime el tablero
        boton = tecla(dificultad) # obtiene la tecla presionado
        if(boton == -1): # si se presionó ESPACIO / ENTER
            continuar = False
        else:
            siguiente = desplazamiento(tablero, serpiente, boton, comida) # mueve la serpiente dependiendo de la entrada

            if(siguiente == 1): # comió la serpiente
                puntos += 1
                hay_comida = False
            elif(siguiente == -1): # hubo colisión
                continuar = False

    return puntos

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
