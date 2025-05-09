"""
Name: chevy_colorado.py
Author: Joseph Freze
Created: 05/08/2025
Purpose: OOP simulator for my 2025 Chevy Colorado
"""

# Making a Truck class to hold all the info about the vehicle
class Truck:
    def __init__(self):
        # TODO: Store the brand of the truck
        self.make = "Chevy"

        # TODO: Store the model name
        self.model = "Colorado"

        # TODO: Store the year the truck was made
        self.year = 2025

        # TODO: Start the speed at 0 because the truck isn't moving yet
        self.speed = 0  # in miles per hour

        # TODO: Later on we might want to add gas level, color, or mileage


# TODO: Make an actual truck from the Truck class
my_truck = Truck()

# TODO: Print something to show the truck is ready
print(f"{my_truck.year} {my_truck.make} {my_truck.model} initialized.")
