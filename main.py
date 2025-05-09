"""
Name: main.py
Author: Joseph Freze
Created: 05/08/2025
Purpose: Main program with user input
"""

# TODO: Import the Truck class from the chevy_colorado file
from chevy_colorado import Truck

# TODO: Create a Truck object
my_truck = Truck()

# TODO: Start a loop so we can keep interacting with the truck
while True:
    # TODO: Show the main menu to the user
    print("\n--- Truck Menu ---")
    print("1. Accelerate")
    print("2. Brake")
    print("3. Honk")
    print("4. Turn on headlights")
    print("5. Turn off headlights")
    print("6. Show truck status")
    print("7. Quit")

    # TODO: Ask the user for their choice
    choice = input("Choose an option (1-7): ")

    # TODO: Handle each option based on what the user typed
    if choice == "1":
        my_truck.accelerate()
    elif choice == "2":
        my_truck.brake()
    elif choice == "3":
        my_truck.honk()
    elif choice == "4":
        my_truck.turn_on_lights()
    elif choice == "5":
        my_truck.turn_off_lights()
    elif choice == "6":
        my_truck.status()
    elif choice == "7":
        # TODO: Exit the program nicely
        print("Exiting the program. See ya!")
        break
    else:
        # TODO: Handle invalid input
        print("Invalid choice. Please pick a number from the menu.")
