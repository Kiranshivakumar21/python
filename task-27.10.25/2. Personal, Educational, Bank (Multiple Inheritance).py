class Personal:
    def __init__(self):
        self.name = input("Enter your name: ")
        self.mail = input("Enter your mail: ")
        self.mobile = int(input("Enter your mobile: "))
        self.address = input("Enter your address: ")
        print(" "*25)

    def info(self):
        print(f"Name: {self.name}")
        print(f"Mail: {self.mail}")
        print(f"Mobile: {self.mobile}")
        print(f"Address: {self.address}")
        print(" "*25)

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
        print(" "*25)

class Bank(Educational):
    def __init__(self):
        super().__init__()
        self.acc_num = input("Enter Account Number: ")
        self.branch_name = input("Enter Branch Name: ")
        self.bank_name = input("Enter Bank Name: ")
        self.ifsc = input("Enter IFSC Code: ")
        self.balance = float(input("Enter Available Balance: "))

    def info(self):
        super().info()
        print(f"Account Number: {self.acc_num}")
        print(f"Branch Name: {self.branch_name}")
        print(f"Bank Name: {self.bank_name}")
        print(f"IFSC Code: {self.ifsc}")
        print(f"Available Balance: {self.balance}")
        print(" "*25)
        

# Usage
print("\n=== Task 2: Personal, Educational, Bank ===")
b = Bank()
b.info()
