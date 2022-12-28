import os
import random

from art import logo

# ______NOTES______
# mode var. 2 modes: easy = 10 lives, hard = 5 lives
# checker() that takes parameter input"guess" and "numb" spits out
# winlose()
# if lives = 0 return you lose
# if lives = -1 return congrats you win!
# lives global variable
# while lives > 0 ----> checker()
# after while loop:
# winlose()
# had to use to access global lives var in some funcs, they say not to but couldnt figure out any other way

lives = 0  # accesed globally inside game_on, checker funcs


def clr():
    """clear scrn function because python is stupid and doesnt have a built in one....."""
    os.system("clear")


def checker(guess, numb):
    """inputs users guess (int) and checks to see if its higher or lower"""
    global lives
    if guess < numb:
        lives -= 1
        return "Too Low"
    if guess > numb:
        lives -= 1
        return "Too High"
    if guess == numb:
        lives = -1


def winlose():
    """test lives after checker to see if user won/lost"""
    if lives == 0:
        return "Ha-Ha you ran out of lives, you lose. stick to checkers, noob!"
    if lives == -1:
        return "Wooptie Doo.... you got the right number, you probably cheated!"


def game_on():
    """main game logic"""

    # init new game - ran numb and game mode
    global lives
    numb = random.randint(1, 100)
    highlow = ''  # just using this as a placeholder in the while loop so i can later print "too high" or "too low"

    mode = input(
        'Do you wanna play hard mode, or are you ganna be a lil sisy and play on easy? (hard/easy)').lower()
    if mode == "hard":
        lives = 5
    elif mode == "easy":
        lives = 10
    else:
        print('you idiot you broke my game... relaunch it cuz im to lazy to code this error catch....')
    clr()

    # number guessing loop
    while lives > 0:
        clr()
        print(logo)
        print(f"lives remaining: {lives}")
        print(highlow)
        guess = int(input("guess a number\n"))
        highlow = checker(guess, numb)

    print(winlose())


clr()
print(logo)
game_on()
