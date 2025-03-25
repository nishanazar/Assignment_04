# # Problem Statement
# # Implement an 'eraser' on a canvas.
# # The canvas consists of a grid of blue 'cells' which are drawn as rectangles on the screen. We then create an eraser rectangle which, when dragged around the canvas, sets all of the rectangles it is in contact with to white.

import tkinter as tk

# Constants
CANVAS_WIDTH = 400
CANVAS_HEIGHT = 400
CELL_SIZE = 40
ERASER_SIZE = 20

def erase(event=None):
    """ Erase the area under the eraser. """
    x, y = canvas.winfo_pointerx() - canvas.winfo_rootx(), canvas.winfo_pointery() - canvas.winfo_rooty()
    canvas.create_rectangle(x, y, x + ERASER_SIZE, y + ERASER_SIZE, fill="white", outline="white")

def start_erasing():
    """ Start erasing when button is clicked. """
    root.bind("<B1-Motion>", erase)  # Bind mouse movement to eraser function

# Create main window
root = tk.Tk()
root.title("Eraser on Canvas")

# Create Canvas
canvas = tk.Canvas(root, width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg="pink")
canvas.pack()

# Draw grid of blue cells
for row in range(0, CANVAS_HEIGHT, CELL_SIZE):
    for col in range(0, CANVAS_WIDTH, CELL_SIZE):
        canvas.create_rectangle(col, row, col + CELL_SIZE, row + CELL_SIZE, fill="pink", outline="black")

# Create a button to start erasing
erase_button = tk.Button(root, text="Start Erasing", command=start_erasing)
erase_button.pack(pady=10)

# Run the Tkinter main loop
root.mainloop()

