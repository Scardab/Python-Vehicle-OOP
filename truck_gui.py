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
root.title("2025 Chevy Colorado Simulator")

# TODO: Create the Truck object
my_truck = Truck()

# TODO: Run the GUI loop
root.mainloop()