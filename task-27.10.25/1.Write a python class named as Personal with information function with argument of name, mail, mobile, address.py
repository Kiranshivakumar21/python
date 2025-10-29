class Personal:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.mail = input("Enter your mail: ")
        self.mobile = int(input("Enter your mobile: "))
        self.address = input("Enter your address: ")

    def info(self):
        print(f"Name: {self.name}")
        print(f"Mail: {self.mail}")
        print(f"Mobile: {self.mobile}")
        print(f"Address: {self.address}")

class Educational(Personal):
    def __init__(self):
        super().__init__()
        self.marks1 = float(input("Enter marks for Tamil : "))
        self.marks2 = float(input("Enter marks for English : "))
        self.marks3 = float(input("Enter marks for Maths : "))
        self.marks4 = float(input("Enter marks for Sciencce : "))
        self.marks5 = float(input("Enter marks for Social-Sciencce : "))
        self.total = self.marks1 + self.marks2 + self.marks3 + self.marks4 + self.marks5
        self.percentage = (self.total / 500) * 100

    def info(self):
        super().info()
        print(f"Marks: {self.marks1}, {self.marks2}, {self.marks3}, {self.marks4}, {self.marks5}")
        print(f"Total: {self.total}")
        print(f"Percentage: {self.percentage:.2f}%")

# Usage
print("=== Task 1: Personal & Educational ===")
ed = Educational()
ed.info()
