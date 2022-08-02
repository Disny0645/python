import random

def Game():
    print("Try to guess the number! Type a number between 1 and 10 below:")
    rawNum1 = input("Enter number: ")
    num1 = int(rawNum1)
    num2 = random.randint(1,10)
    num2str = str(num2)
    if num1 == num2:
        print("Congratulations! You won!")
    else:
        print("Sorry you lost ): The correct number was: " + num2str)
    print("Would you like to play again?")
    ans = input("Answer(y/n): ")
    if ans == "y":
        Game()
    else:
        print("Aww, see you again soon!")
Game()