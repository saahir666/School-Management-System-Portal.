import person
    
class Student(person):
    def __init__(self, name, age, studend_class, fee_paid, fee_amount, midterm, final, progress):
        super().__init__(name, age)
        self.student_class = studend_class
        self.fee_paid = fee_paid
        self.fee_amount = fee_amount
        self.midterm = midterm
        self.final = final 
        self.progress = progress 
        
    def display(self):
        print(f"Student Name: {self.name}, Student Age: {self.age}, Student Class: {self.student_class}")
        print(f"Fee Paid: {self.fee_paid}, Fee Amount: {self.fee_amount}, Midterm: {self.midterm}")
        print(f"Final: {self.final}, Progress: {self.progress}")
        print("-" * 40)
        
        
    def to_row(self): 
        return f"{self.name}, {self.age}, {self.student_class}, {self.fee_paid}, {self.fee_amount}, {self.midterm}, {self.final}, {self.progress}"       