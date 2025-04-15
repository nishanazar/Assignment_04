import os

def main():
    
    i = 0
    path = "F:/Generative_AI_Course/Python_class/images_rename/"
   
    try:
        user_input : str = str(input("\nEnter a Filename: ")).strip()

        if user_input.isdigit():
            raise ValueError("Please enter a name that contains at least one letter.")
    
    except ValueError as ve:
       print("❌ Error:", ve)

    for filename in os.listdir(path):
        my_dest = user_input + str(i) +".jpg"
        my_source =path + filename
        my_dest =path + my_dest
        os.rename(my_source, my_dest)
        i += 1

if __name__ == "__main__":
    main()