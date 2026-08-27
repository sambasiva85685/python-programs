#1
# def greet():
#     print("hello Student")
# def mydecor(func):
#     def inner():
#         print("Before function execution")
#         func()
#         print("After function execution")
#     return inner
# a=mydecor(greet)
# a()
#
# #2
# def greet():
#     print("Good morning")
# def mydecor(func):
#     def inner():
#         print("Welcome Message")
#         func()
#         print("Thank You Message")
#     return inner
# a=mydecor(greet)
# a()
#
# #3
# def my_decor(func):
#     def greet(a,b):
#         print("Addition result:",end="")
#         func(a,b)
#     return greet
# @my_decor
# def add(a,b):
#     print(a+b)
# add(10,20)
#
# #4
# def check_number(func):
#     def greet(a):
#         if a%2==0:
#             print("Even number")
#         else:
#             print("Odd number")
#         func(a)
#     return greet
# @check_number
# def show(a):
#     print("Number accepted")
# show(2)
#
#5
user_name="samba siva"
user_password="Siva@143"
def login_required(func):
    def inner():
        input1=input("enter name:")
        input2=input("enter password:")
        if input1==user_name and input2==user_password:
            print("access granted")
            func()
        else:
            print("please login first")
    return inner
@login_required
def profile():
    print("Welcome to profile")  
profile()
#
#
#
# #6
# import functools
# def mydecor(func):
#     @functools.wraps(func)
#     def inner():
#         print("Welcome Message")
#         func()
#         print("Thank You Message")
#     return inner
# @mydecor
# def greet():
#     print("Good morning")
# greet()
# print(greet.__name__)
from enum import nonmember


#7
# def decor(func):
#     def wrapper(*args,**kwargs):
#         print("hello mawa")
#         func(*args,**kwargs)
#         print("money kavali")
#     return wrapper
# @decor
# def add(a,b,c):
#     print(a,b,c)
# add(10,20,30)
#
#8
def validate_positive(func):
    def wrapper(*args):
        for i in args:
            if i<0:
                print("Error negative arguments are not allowed")
                return None
        return func(*args)
    return wrapper
@validate_positive
def multiply(a,b):
    return a * b
print(multiply(10,20))
print(multiply(-10,2))



