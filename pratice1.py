#1
class car:
    brand="Toyato"
    def show_brand(self):
        print(self.brand)
        print(car.brand)
obj=car()
obj.show_brand()

#2
class book:
    title="python programming"
    def details(self):
        print(self.title)
obj1=book()
obj1.details()

#3
class mobile:
    pass
obj3=mobile()
obj.brand="samsung"
obj.price=200000
print(obj.brand,obj.price)

#4
class Employee:
    pass
obj4=Employee()
obj3=Employee()
obj2=Employee()
print(id(obj4))
print(id(obj4))
print(id(obj4))

#5
class Employee:
    def __init__(self):
        self.name="siva"
        self.salary=250000
obj5=Employee()
print(obj5.name)
print(obj5.salary)

#6
class laptop:
    brand="lenovo"
    ram=16
    price=47000
lap=laptop()
print(lap.brand)
print(lap.ram)
print(lap.price)

#7
class bankaccount:
    account_holder="siva"
    balance=10000
obj6=bankaccount()
obj7=bankaccount(1000)
print(obj6.account_holder)
print(obj7.balance)
