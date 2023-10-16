class Student:

    student_list = ["Jullunar", "Ayman", "Ali"]
    user_input = input("Please Enter student name: ").capitalize().strip()
    def __init__(self, first_name, last_name, id, gender):
        self.fname = first_name
        self.lname = last_name
        self.id = id
        self.gender = gender
        
    print("Welcome to Student Management System")
    
    def accept_fun(self):
        if self.fname in self.student_list:
            print(f"Student {self.fname} is accepted")
        else:
            print(f"Student {self.fname} is rejected")
            
    def get_student_info(self):
        print(f"Student name is {self.fname} {self.lname}, student id is {self.id} and student gender is {self.gender}")
        
Student_one = Student("Jullunar", "Khalil", "123", "female")
print(Student.accept_fun(Student_one))
print(Student.get_student_info(Student_one))