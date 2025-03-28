import random
from hangman_word import words
import string


def get_valid_number(words):
    word = random.choice(words)
    while "_" in word or " " in word:
        word = random.choice(words)

    return word

def hangman():
    word = get_valid_number(words)
    word_letters = set(word)
    alphabet = set(string.ascii_lowercase)
    used_letters = set()

    lives = 6

    while len(word_letters) > 0 and lives > 0:
        
        space = " "
        print(f"You have {lives} lives left and You have used these letters: {space.join(used_letters)}")

        word_list = [letter if letter in used_letters else "_" for letter in word]
        print("Current word: ", " ".join(word_list))
        user_letter = input("Guess a letter: ").lower()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)

            if user_letter in word_letters:
                word_letters.remove(user_letter)

            else:
                lives = lives -1

        elif user_letter in used_letters:
            print("You have already used that character. Please try again.")

        else:
            print("Invalid character. Please try again.")
    if lives == 0:
        print(f"You died, sorry. The word was, {word}")
    else:
        print(f"You guessed the word {word} !!")

hangman()