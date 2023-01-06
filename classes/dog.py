class Dog:

    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


my_dog = Dog("Black", 6)
my_dog = Dog("Doggie", 56)
my_dog = Dog("Zoha", 34)

print(my_dog.sit())
print(my_dog.roll_over())
