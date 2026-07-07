#def greet(name):
    #print("hello",name)
#welcome=greet
#welcome("siva")


#def square(n):
 #   return n**2
#s=square
#print(s(6))

#def message():
  #  print("hello python")
#s=message
#s()
#s()
#s()

#count=len
#list=[10,30,50]
#print(count(list))


#display=print
#display("functional referencr")


##def apply(func,value):
#   return  func(value)
#def cube(n):
#    return n**3
#print(apply(cube,5))



#def add(a,b):
    #return a+b
#def subtract(a,b):
 ##   return a-b
#def calculator( a,b,operation):
#    return operation(a,b)
#print(calculator(10,5,add))
#print(calculator(10,5,subtract))


def is_even(num):
   return num%2==0
def check(num,func):
    return func(num)
print(check(8,is_even))
print(check(7,is_even))
