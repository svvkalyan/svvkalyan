class Bird:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Mammal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Bat(Bird, Mammal):
    def speak(self):
        return f"{self.name} says Screech!"

bat = Bat("Batty")
print(bat.speak())  # Output: Batty says Screech!