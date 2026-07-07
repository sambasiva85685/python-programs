#1
a=["a","b","c"]
print(list(map(lambda x:ord(x),a)))

#2
a=[[1,2],[3,4],[5,6]]
print(list(map(lambda x:list(map(lambda y:y+5,x)),a)))

#3
nums=[12,15,7,18,20,21,25]
print(list(filter(lambda x: x%3 ^ x%5,nums)))

#4
a="samba"
print(list(filter(lambda x:x.lower() not in "aeiou",a)))

#5
a=["p","y","t","h","o","n"]
from functools import reduce
print(reduce(lambda x,y:x+y,a))

#6
a=[5,10,15,20,25,30]
from functools import reduce
print(reduce(lambda x,y:x+y,(sorted(list(filter(lambda x:x%5==0,list(map(lambda x:x**2,a)))),reverse=True))))

#1
def order(product,quantity=1,price=100):
    print("product is",product)
    print("quantity is",quantity)
    print("price is",price)
order("pizza")
order("juice",20,500)
order(product="watch",quantity=5,price=10000)

#2
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def math_operation(a,b,operation):
    return operation(a,b)
print(math_operation(2,5,mul))
print(math_operation(3,5,div))

#3
num=lambda x:"positive" if x>0 else ("negative" if x<0 else "zero")
print(num(-7))

#4
def calculate(a,b,operation):
    def add():
        return a+b
    def sub():
        return a-b
    def mul():
        return a*b
    def div():
        return a/b
    def mod():
        return a%b
    if operation=="+":
        print(add())
    elif operation=="-":
        print(sub())
    elif operation=="*":
        print(mul())
    elif operation=="/":
        print(div())
    elif operation=="%":
        print(mod())
calculate(10,20,"+")
calculate(10, 20, "-")
calculate(10, 20, "*")
calculate(10, 20, "/")
calculate(10, 20, "%")






