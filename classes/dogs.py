class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"hi my name is {self.name} am {self.age} years old."

    def speak(self, sound):
        """This print out the baking sound the that type of breed of dog make when you pass sound"""
        return f"this is how {self.name} sounds {sound}"


class Pug(Dog):
    def speak(self, sound="wioo"):
        """This print out the baking sound the that type of breed of dog make when you pass sound"""
        return f"this is how {self.name} sounds {sound}"


class Puddle(Dog):
    def speak(self, sound="woo woo"):
        """This print out the baking sound the that type of breed of dog make when you pass sound"""
        return f"this is how {self.name} sounds {sound}"


class Shepherd(Dog):
    def speak(self, sound="WOOOOO"):
        """This print out the baking sound the that type of breed of dog make when you pass sound"""
        return f"this is how {self.name} sounds {sound}"


class Rottweiler(Dog):
    def speak(self, sound="WOOOOOOO"):
        """This print out the baking sound the that type of breed of dog make when you pass sound"""
        return f"this is how {self.name} sounds {sound}"


class Bull(Dog):
    pass


dog_1 = Rottweiler("annny", 4)
dog_1 = dog_1.speak()

print(dog_1)

dog_2 = Shepherd("amazing", 5)
dog_2 = dog_2.speak()
print(dog_2)


dog_3 = Bull("stanley", 5)
print(dog_3)
dog_3 = dog_3.speak('HOWOHOO')
print(dog_3)

