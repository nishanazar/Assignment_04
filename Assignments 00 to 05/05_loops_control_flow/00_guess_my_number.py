# Problem Statement
# Guess My Number

# I am thinking of a number between 0 and 99... Enter a guess: 50 Your guess is too high

# Enter a new number: 25 Your guess is too low

# Enter a new number: 40 Your guess is too low

# Enter a new number: 45 Your guess is too low

# Enter a new number: 48 Congrats! The number was: 48

import random
def main():

    secret_number = random.randint(0, 90)
    print("I am thinking of a number between 1 and 99...")


    user_input = int(input("Enter a guess: "))


    while user_input != secret_number:
   
    
        if secret_number > user_input:
            print("Your guess is too low!")

        elif secret_number < user_input:
            print("Your guess is too high!")
        print()
    
        user_input = int(input("Enter a new number: "))

    print(f"Congrats! The number was: {secret_number}")


if __name__ == '__main__':
    main()