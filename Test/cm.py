from pm import ParentClass

class ChildClass(ParentClass):
    def __init__(self, value, marks, extra_data):
        super().__init__(value, marks)  # Call the parent's constructor
        self.extra_data = extra_data

    def display(self):
        return f"Child value: {self.value}, Extra data: {self.extra_data},{self.marks} "
