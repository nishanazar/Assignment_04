# Problem Statement
# Guess My Number
# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is 
# too high
# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

import random

def main():
    random_number = random.randint(0, 99)

    while True:
        guessed_number = int(input("Guess the number: "))

        if(guessed_number < random_number):
            print("Your guess is too low")

        elif(guessed_number > random_number):
             print("Your guess is too high")

        else:
            print("You guess is correct")
            break
if __name__ == '__main__':
    main()