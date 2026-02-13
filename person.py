class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
    def display(self):
        return f"{self.name}, {self.age}"
