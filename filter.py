#def check(n):
  #  if n%2==0:
   #     return n
#print(list(filter(check,[2,3])))

#print(list(filter(lambda x: x%2==0,[2,3])))

#def f1(n):
 #   if n%2!=0:
  #      return n
#print(list(filter(f1,[1,2,3,4,5])))

#print(list(filter(lambda x: x%2!=0,[1,2,3,4,5,6])))

#def f1(n):
#    if n>10:
 #       return n
#print(list(filter(f1,[1,2,10,11,12,13])))

#def f1(a):
#    return len(a)>4
#a=["siva","prudhvi"]
#print(list(filter(f1,a)))


#print(list(filter(lambda x: len(x)>4,["siva","prudhvi"])))

#def f1(n):
 #   return n
#n=["siva"]
#print(list(filter(f1,n)))

#def f1(n):
 #   return n.lower() in "aeiou"
#a="samba siva"
#print(list(filter(f1,a)))

print(list(filter(lambda x:x.lower() not in "aeiou","samba siva")))

##print(list(filter(lambda x:(x%5==0)^(x%3==0),nums)))


#print(list(filter(lambda x: x>10,[11,12,10])))

#def f1(n):
#    if n%5==0:
 #       return n
#print(list(filter(f1,[1,2,3,4,5])))

#print(list(filter(lambda x: x%5==0,[1,2,3,4,5])))


