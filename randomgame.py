import sys
import random

arg1 = int(sys.argv[1])
arg2 = int(sys.argv[2])

answer = random.randint(arg1,arg2)

while True:
    try:
        guess = input(f"Please enter a name on range {arg1}-{arg2}\n")
        x = int(guess)
        if x >= int(arg1) and x <= int(arg2):
            if x == answer:
                print("Congratulations!! You've guessed the value.")    
            else:
                print("Ups, try again")
        else:
            print("You've entered an invalid number")
    except ValueError:
        print("Please enter a number.")