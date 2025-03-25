# Problem Statement
# There's a small fruit shop nearby your house that you like to buy from. Since you buy several
# fruit at a time, you want to keep track of how much the fruit will cost before you go. Luckily
# you wrote down what fruits were available and how much one of each fruit costs.
# Write a program that loops through a dictionary of fruits, prompting the user to see how many 
# of each fruit they want to buy, and then prints out the total combined cost of all of the fruits.
# Here is an example run of the program (user input is in bold italics):
# How many (apple) do you want?: 2
# How many (durian) do you want?: 0
# How many (jackfruit) do you want?: 1
# How many (kiwi) do you want?: 0
# How many (rambutan) do you want?: 1
# How many (mango) do you want?: 3
# Your total is $99.5

def main():
    total_cost = 0
    fruits = {
    'apple': 1.5,
    'durian': 50, 
    'jackfruit': 80,
    'kiwi': 1, 
    'rambutan': 1.5, 
    'mango': 5
    }

    for fruit_name in fruits:
        price = fruits[fruit_name]
        
        amount_bought = int(input(f"How many ({fruit_name}) do you want?: "))

        total_cost += price * amount_bought
    print(f"Your total is ${total_cost}")

if __name__ == '__main__':
    main()