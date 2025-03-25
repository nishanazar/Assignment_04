# Problem Statement
# Simulate rolling two dice, and prints results of each roll as well as the total.
import random
NUM_SIDES: int = 6
def main():
    die1: int = random.randint(1, NUM_SIDES)
    die2: int = random.randint(1, NUM_SIDES)
    
    
    total: int = die1 + die2
    
    
    print(f"Dice have {NUM_SIDES} sides each.")
    print(f"First die: {die1}")
    print(f"Second die: {die2}")
    print(f"Total of two dice: {total}")


if __name__ == '__main__':
    main()