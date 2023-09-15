class Grandparent:
    def __init__(self, name):
        self.name = name

    def speak(self):
        pass

class Parent(Grandparent):
    def speak(self):
        return f"{self.name} says Hello from Parent!"

class Child(Parent):
    def speak(self):
        return f"{self.name} says Hi from Child!"

child = Child("Alice")
print(child.speak())  # Output: Alice says Hi from Child!