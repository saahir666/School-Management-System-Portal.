class ParentClass:
    def __init__(self, value, marks):
        self.value = value
        self.marks = marks

    def display(self):
        return f"{self.value}, {self.marks}"
