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
