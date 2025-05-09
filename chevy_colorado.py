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

    # TODO: Let the truck start moving by accelerating
    def accelerate(self):
        # Increase the speed by 10 each time this method is called
        self.speed += 10
        print(f"Accelerating... Current speed: {self.speed} mph")

        # TODO: Add a way to slow the truck down
    def brake(self):
        # Decrease speed by 10, but not below 0
        if self.speed >= 10:
            self.speed -= 10
        else:
            self.speed = 0
        print(f"Braking... Current speed: {self.speed} mph")

# TODO: Make an actual truck from the Truck class
my_truck = Truck()

# TODO: Print something to show the truck is ready
print(f"{my_truck.year} {my_truck.make} {my_truck.model} initialized.")

# TODO: Try accelerating the truck and see how fast it goes
my_truck.accelerate()

# TODO: Try braking the truck to slow it down
my_truck.brake()