import random  

def RockPaperScissor():
    print("This is rock paper scissors, please enter your choice below:")
    
    rawPlayerAns = input("Answer (r/p/s): ") 
    botAns = random.randint(1,3) #I decided to use numbers instead of strings for simplicity

    if botAns == 1: #this is for debugging 
        botAnsStr = "rock"
    elif botAns == 2:
        botAnsStr = "paper"
    elif botAns == 3:
        botAnsStr = "scissors"


    if rawPlayerAns == "r":
        playerAns = 1
    elif rawPlayerAns == "p":
        playerAns = 2
    elif rawPlayerAns == "s":
        playerAns = 3
    else:
        print("somethign went wrong, restarting program...") #Just a precaution
        RockPaperScissor()

    if playerAns == botAns: #This gave me a headache
        print("It's a tie")
    elif playerAns - 1 == botAns or playerAns + 2 == botAns:
        print("You win!!! (:")
        print("The bot answered " + botAnsStr) 
    elif botAns - 1 == playerAns or botAns + 2 == playerAns:
        print("You lose... ):")
        print("The bot answered " + botAnsStr) 
    else:
        print("somethign went wrong, restarting program...") #another precaution
        RockPaperScissor()
    
    print("Do you want to play again? (y/n): ")
    playerAnsAgain = input()
    if playerAnsAgain == "y":
        RockPaperScissor()
    else:
        print("Ok, see you soon!!!")

    #I sorta want to make a script with multiple games where you can choose wich ones you want to play...

    

RockPaperScissor()
    