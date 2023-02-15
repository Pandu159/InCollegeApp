# import json
# from authentication import *
from feed import *


def main():
    HomeScreen()
    print("Input 9 to view a video that would explain why joining InCollege would be highly beneficial for you")
    selection = int(input("To create an account, input 0, to sign in input 1: "))

    userName = None

    if selection == 0:
        userName = signUp()
    elif selection == 1:
        userName = signIn()
    elif selection == 9:
        print("Video is now playing!")
        main()
    elif selection == 2:  # Delete later
        exit(-1)
    else:
        print("Invalid Selection!")
        exit(-1)

    if userName is not None:
        selectOption(userName)


#main()
