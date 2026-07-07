#1
def greet():
    print("hello Student")
def mydecor(func):
    def inner():
        print("Before function execution")
        func()
        print("After function execution")
    return inner
a=mydecor(greet)
a()

#2
def greet():
    print("Good morning")
def mydecor(func):
    def inner():
        print("Welcome Message")
        func()
        print("Thank You Message")
    return inner
a=mydecor(greet)
a()

#3
def my_decor(func):
    def greet(a,b):
        print("Addition result:",end="")
        func(a,b)
    return greet
@my_decor
def add(a,b):
    print(a+b)
add(10,20)

#4
def check_number(func):
    def greet(a):
        if a%2==0:
            print("Even number")
        else:
            print("Odd number")
        func(a)
    return greet
@check_number
def show(a):
    print("Number accepted")
show(2)

