"""
Name: truck_gui.py
Author: Joseph Freze
Created: 05/08/2025
Purpose: Creating a basic GUI for the truck program
"""

# TODO: Import tkinter and your Truck class
from tkinter import * # I learned that importing * brings in all tkinter classes and functions!
from chevy_colorado import Truck

# TODO: Create the main window
root = Tk()
root.geometry("1400x800")  # width x height in pixels
root.title("2025 Chevy Colorado Simulator")

# TODO: Load and display the truck image
from tkinter import PhotoImage

# Load the image
truck_img = PhotoImage(file="colorado.png")

# Create a label with the image and pack it
image_label = Label(root, image=truck_img)
image_label.pack(pady=10)

# TODO: Create the Truck object
my_truck = Truck()

# TODO: Label to show truck speed
status_label = Label(root, text=f"Speed: {my_truck.speed} mph", font=("Arial", 14))
status_label.pack(pady=10)

# TODO: Run the GUI loop
root.mainloop()