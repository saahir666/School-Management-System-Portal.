from teacher import Teacher
from student import Student

class SchoolManagementSystem:
    def __init__(self):
        self.teachers = []
        self.students = []
        
        
    def add_teacher(): 
        print("\n ==== Enter Teacher Details ====")
        name = input("Enter Your Name: ")
        age = input("Enter your age: ")
        subject = input("Enter your subject: ")
        classes = input("Enter your class: ")
        hours = input("Enter your hours: ")
        salary = input("Enter your salary: ")
        
        self.teachers.append(Teacher(name, age, subject, classes, hours, salary))
        
        
    def add_student(self):
        print("\n ==== Enter Student Details ==== ")
        name = input("Enter your Name: ")
        age = input("Enter you age: ")
        student_class = input("Enter your Class: ")
        fee_paid = int(input("Enter your Fee Paid: "))
        fee_amount = int(input("Enter your fee Amount: "))
        midterm = input("Enter your Midterm Marks: ")
        final = input("Enter your Final Marks: ")
        progress = input("Progress: (Good/Average)")
        
        
        self.student.append(Student(name, age, student_class, fee_paid, fee_amount, midterm, final, progress))
        
    def display_all(self): 
        print("\n === Teacher Record === ")
        for t in self.teachers:
            t.display()
        print("\n === Student Record === ") 
        for s in self.students: 
            s.display()
            
    def save_to_file(self, filename="record.txt"):
        with open(filename, "w") as f:
            f.write("=== Teachers Record === \n")
            f.write("Name, Age, Subject, Classes, Hours, Salary")
            for t in self.teachers: 
                f.write(t.to_row() + "\n")
                
                
            f.write("\n === Student Records === ")
            f.write("Name, Age, Class, Fee Paid, Fee Amount, Midterm, Final, Progress\n")
            for s in self.students: 
                f.write(s.to_row() + "\n")
                
        print(f"\n Data Save Successfully to {filename}!")
        