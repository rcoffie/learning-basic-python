class Car:
    """A simple attempt to represent a car"""

    def __init__(self, make, model, year):
        """initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


my_new_car = Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())


# Setting a Default value for an Attribute


class Car:
    def __init__(self, make, model, year):
        """initialize attributes to describe a car."""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage ."""
        print(f"This car has {self.odometer_reading} miles on it ")


my_old_car = Car("BMW", "X6", "1998")
print(my_old_car.get_descriptive_name())
my_old_car.read_odometer()

# Modifying an Attribute’s Value Directly
my_old_car.odometer_reading = 23 
my_old_car.read_odometer()