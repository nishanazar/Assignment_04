# Welcome to the High-Low Game!
# Round 1 Your number is 1 Do you think your number is higher or lower than the
# computer's?: even Please enter either higher or lower: lower You were right!
# The computer's number was 6 Your score is now 1

# Extension #2: Conditional ending messages
# Add conditional messages at the end which gauge players on how they performed!
# For ours, we evaluated the player and gave them separate messages if:

# they had a perfect game

# ... Your score is now 5

# Wow! You played perfectly!

# they won at least half the rounds (rounded down)

# ... Your score is now 2

# Good job, you played really well!

# they won less than half the rounds

# ... Your score is now 1

# Better luck next time!


import random

num_round = 5
score = 0
print("Welcome to the High-Low Game!")
print("-" * 30)
for round_num in range(1, num_round + 1):
    


  my_number = random.randint(1, 100)
  computer_number = random.randint(1, 100)

  print("-"* 30)
  print("Round", round_num)
  print("-"* 30)


  print(f"Your number is: {my_number}")

  user_guess = input("Do you think your number is higher or lower than the computer's?:  ")

  if((user_guess == "higher" and computer_number > my_number)
   or
  (user_guess == "lower" and computer_number < my_number)):
    print(f"You got a point +1 The computer number is {computer_number}")
    score += 1
  else:
    print(f"wrong guess , The computer number is {computer_number}")

    if (score == num_round):
      print("Wow! you played perfectly")
    elif (score > 2):
      print("Good job, You played well")
    else:
      print("next time you will do better")

print(f"Your final score is: {score}")
print("Thanks for playing!")