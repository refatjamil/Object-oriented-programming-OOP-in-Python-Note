# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def view_name(self):
        print(f"Name: {self.name}")

# Derived class
class Dog(Animal):
    def view_dog_name(self):
        super().view_name() 
        

dog_instance = Dog("Buddy")

dog_instance.view_dog_name()     # Output: Buddy barks
# dog_instance.view_dog_color()     # Output: Buddy barks
