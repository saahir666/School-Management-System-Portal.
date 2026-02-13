from person import Person

class Teacher(Person):
    def __init__(self, name, age, subject, classes, hours, salary):
        super().__init__(name, age)  # ✅ Calls Person.__init__()
        self.subject = subject
        self.classes = classes
        self.hours = hours
        self.salary = salary
        
    def display(self):
        # ✅ self.name and self.age are accessible here
        return f"{self.name}, {self.age}, {self.subject}, {self.classes}, {self.hours}, {self.salary}"
