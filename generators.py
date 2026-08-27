#1
def num(n):
    for i in range(1,n+1):
        yield i
a=num(5)
for i in a:
    print(i)

#2
def numbers(n):
    for i in range(1,n+1):
        if i%2==0:
            yield i
b=numbers(5)
for i in b:
    print(i)


#3
def chr(n):
    for i in range(0,len(n)):
        yield n[i]
c=chr("Siva")
for i in c:
    print(i)


#4
def chr(n):
    for i in range(0,len(n)):
        if n[i] in "aeiou":
            yield n[i]
c=chr("Siva")
for i in c:
    print(i)
#
#5
def digit(n):
    for i in range(0,len(n)):
        if n[i].isdigit():
            yield n[i]
c=digit("Siva33")
for i in c:
    print(i,end=" ")

#6
def sq(n):
    for i in range(0,len(n)):
            yield n[i]**2
l=list(map(int,input().split()))
c=sq(l)
for i in c:
    print(i,end=" ")

#7
def dig(n):
    while n>0:
        r=n%10
        n=n//10
        yield r
a=dig(277)
for i in a:
    print(i)

#8
def rev(n):
    for i in range(len(n)-1,-1,-1):
        yield n[i]
a=rev("Siva")
for i in a:
    print(i)

#9
def cumulative(n):
    sum=0
    for i in range(0,len(n)):
        sum=sum+n[i]
        yield sum
l=[1,2,3]
a=cumulative(l)
for i in a:
    print(i)


