class School:
    def __init__(self):
        self.name = input("Enter name: ")
        self.mail = input("Enter mail: ")
        self.mobile = int(input("Enter mobile: "))
        self.address = input("Enter address: ")

        
    def info(self):
        if role == Staff:
           print("STAFF DETAILS")
        else: role == Student
        print("STUDENT DETAILS")
           
        print(f"Name: {self.name}")
        print(f"Mail: {self.mail}")
        print(f"Mobile: {self.mobile}")
        print(f"Address: {self.address}")
        

class Staff(School):
    def __init__(self):
        super().__init__()
        self.dept = input("Enter department: ")

    def staffInformation(self):
        self.info()
        print(f"Department: {self.dept}")
        print (" "*25)

class Student(School):
    def __init__(self):
        super().__init__()
        self.dept = input("Enter department: ")
        print (" "*25)

    def studentInformation(self):
        self.info()
        print(f"Department: {self.dept}")

# Usage with user choice
print("\n=== Task 3: School, Staff, Student ===")
role = input("Are you Staff or Student? (type 'Staff' or 'Student'): ").strip().lower()
if role == "staff":
    print("ENTER STAFF DETAILS")
    person = Staff()
    person.staffInformation()
    
elif role == "student":
    print("ENTER STUDENT DETAILS")
    person = Student()
    person.studentInformation()
    
else:
    print("Invalid option")
