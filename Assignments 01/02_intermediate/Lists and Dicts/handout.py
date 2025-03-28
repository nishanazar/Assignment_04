# Problem #1: List Practice
# Now practice writing code with lists! Implement the functionality described in 
# the comments below.

# def main(): # Create a list called fruit_list that contains the following 
# fruits: # 'apple', 'banana', 'orange', 'grape', 'pineapple'.

# Print the length of the list.


# Add 'mango' at the end of the list. 


# Print the updated list.

def access_element(lst, index):
    """Returns the element at the given index or an error message if out of range."""
    try:
        return lst[index]
    except IndexError:
        return "Error: Index out of range."

def modify_element(lst, index, new_value):
    """Modifies the element at the given index with a new value, ensuring correct data type."""
    try:
        lst[index] = int(new_value)  # Convert input to integer
        return f"Updated list: {lst}"
    except IndexError:
        return "Error: Index out of range."
    except ValueError:
        return "Error: Invalid input. Please enter a valid number."

def slice_list(lst, start, end):
    """Returns a sliced portion of the list based on user input."""
    return lst[start:end]

def index_game():
    """Main function to interact with the user and perform list operations."""
    lst = [1, 2, 3, 4, 5]  # Example list
    print("\n📌 **Welcome to Index Game!**")
    print("Current list:", lst)

    while True:
        print("\nChoose an operation: access | modify | slice | exit")
        operation = input("Enter operation: ").strip().lower()

        if operation == "access":
            try:
                index = int(input("Enter index to access: "))
                print("Result:", access_element(lst, index))
            except ValueError:
                print("Error: Please enter a valid number.")

        elif operation == "modify":
            try:
                index = int(input("Enter index to modify: "))
                new_value = input("Enter new value: ")
                print(modify_element(lst, index, new_value))
            except ValueError:
                print("Error: Please enter a valid number.")

        elif operation == "slice":
            try:
                start = int(input("Enter start index: "))
                end = int(input("Enter end index: "))
                print("Sliced List:", slice_list(lst, start, end))
            except ValueError:
                print("Error: Please enter valid numbers.")

        elif operation == "exit":
            print("👋 Exiting the Index Game. Goodbye!")
            break

        else:
            print("❌ Invalid operation. Please try again.")

if __name__ == "__main__":
    index_game()
