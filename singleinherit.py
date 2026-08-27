# class Bank:
#     def __init__(self,balance):
#         self.balance=balance
#     def deposit(self,amount):
#         self.balance+=amount
#         print(f"deposit amount is {amount},available is {self.balance}")
#     def withdraw(self,amount):
#         if amount<=self.balance:
#             self.balance-=amount
#             print(f"withdraw amount {self.balance}")
#         else:
#             print("Insufficient funds")
#     def check_balance(self):
#         print(self.balance)
# class user(Bank):
#     def __init__(self,name,balance):
#         self.name=name
#         super().__init__(balance)
#         print(f"name is {self.name}")
# obj=user("Samba Siva",10000)
# obj.deposit(1500)
# obj.withdraw(5000)
# obj.check_balance()

# 2
# class Employee:
#     def __init__(self,emp_name,salary):
#         self.emp_name=emp_name
#         self.salary=salary
#     def display_details(self):
#         print("Employee profile")
#         print("Name:",self.emp_name)
#         print("Salary:",self.salary)
# class manager(Employee):
#     def __init__(self,emp_name,salary,pf):
#         self.pf=pf
#         super().__init__(emp_name,salary)
#         #self.pf=pf
#     def bonus(self):
#         self.salary=self.salary+self.pf
#         print("After adding the bonus",self.salary)
# obj1=manager("Siva",100000,10000)
# obj1.display_details()
# obj1.bonus()
#
# #3
class student:
    def __init__(self,Name,marks):
        self.Name=Name
        self.marks=marks
    def display_marks(self):
       # print("student profile")
        print("Student name:",self.Name)
        print("Student marks:",self.marks)
class Result(student):
    def __init__(self,Name,marks):
        super().__init__(Name,marks)
    def calculates(self):
        if self.marks>=35:
            print("Passed")
        else:
            print("failed")
Name=input("enter name:")
marks=int(input("enter marks:"))
obj=Result(Name,marks)
obj.display_marks()
obj.calculates()