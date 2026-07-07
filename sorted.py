#a=["hello","siva","whatups"]
#print(sorted(a,key=lambda x:len(x)))
#print(sorted(a))
#print(sorted(a,reverse=True))

#=[("python",12),("hello",67),("cls",42)]
#print(sorted(a,key=lambda x:x[1]))

d={'siva':23,'prudhvi':22,'meghana':21}
#print(sorted(d))
print(sorted(d.items(),key=lambda x:x[1]))

#a=[1,2,3,4,5]
#print(sorted(a,key=lambda x:x,reverse=True))

a=["banana","apple","mango","grapes"]
print(sorted(a))

a=["samba","siva","sandeep"]
print(sorted(a,key=lambda x:len(x)))

#s="samba"
#print(sorted(s,key=lambda x:x))



#a=[5,10,15,20,25,30]
#from functools import reduce
#print(reduce(lambda x,y:x*y,sorted(filter(lambda x:x%5==0,list(map(lambda x:x+5,a))),reverse=True)))
a=[5,10,15,20,25,30]
from functools import reduce
print(reduce(lambda x,y:x*y,sorted(filter(lambda x:x%5==0,list(map(lambda x:x+5,a))),reverse=True)))
