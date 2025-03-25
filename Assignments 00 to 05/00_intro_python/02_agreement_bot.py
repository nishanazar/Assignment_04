# Problem Statement
# Write a program which asks the user what their favorite animal is, and then always responds with "My favorite animal is also ___!" (the blank should be filled in with the user-inputted animal, of course).

# Here's a sample run of the program (user input is in bold italics - note the space between the prompt and the user input!):

# What's your favorite animal? cow

# My favorite animal is also cow!


def main():
    favourite_animal = input("What's your favourite animal? ").lower()
    print(f"My favorite animal is also {favourite_animal}!")

if __name__ == '__main__':
    main()
