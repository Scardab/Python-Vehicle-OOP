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
root.geometry("1400x1000")  # width x height in pixels
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

# TODO: Function to update the status label
def update_status():
    status_label.config(
        text=f"Speed: {my_truck.speed} mph | Headlights: {'ON' if my_truck.lights_on else 'OFF'}"
    )

# TODO: Accelerate the truck
def handle_accelerate():
    my_truck.accelerate()
    update_status()

# TODO: Brake the truck
def handle_brake():
    my_truck.brake()
    update_status()

# TODO: Honk the horn and update the status label
def handle_honk():
    my_truck.honk()
    status_label.config(text="Honk Honk!")

# TODO: Turn on headlights
def handle_lights_on():
    my_truck.turn_on_lights()
    update_status()

# TODO: Turn off headlights
def handle_lights_off():
    my_truck.turn_off_lights()
    update_status()

# TODO: Buttons for each truck feature
# Accelerate Button
btn_accelerate = Button(root, text="Accelerate", command=handle_accelerate)
btn_accelerate.pack(pady=5)

#Brake Button
btn_brake = Button(root, text="Brake", command=handle_brake)
btn_brake.pack(pady=5)

# Horn Button
btn_honk = Button(root, text="Honk Horn", command=handle_honk)
btn_honk.pack(pady=5)

# Light On Button
btn_lights_on = Button(root, text="Turn On Headlights", command=handle_lights_on)
btn_lights_on.pack(pady=5)

# Light Off Button
btn_lights_off = Button(root, text="Turn Off Headlights", command=handle_lights_off)
btn_lights_off.pack(pady=5)

# TODO: Run the GUI loop
root.mainloop()