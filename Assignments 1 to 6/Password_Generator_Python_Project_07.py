import random 

print("Welcome To your Password Generator")
print("=" *30)

chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*().,?0123456789"

number = int(input("Amount of passwords to generate: "))
length = int(input("Input your password length: "))

print("\nhere are your passwords: ")

for pwd in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    print(passwords)