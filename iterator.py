#1
# n=int(input())
# class Custom:
#     def __init__(self,n):
#         self.n=n
#         self.num=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num<=n:
#             value=self.num
#             self.num+=1
#             return value
#         else:
#             raise StopIteration
# a=Custom(n)
# for i in a:
#     print(i)

#2
# n=int(input())
# class Custom:
#     def __init__(self,n):
#         self.n=n
#         self.num=n
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.num>=1:
#             value=self.num
#             self.num-=1
#             return value
#         else:
#             raise StopIteration
# a=Custom(n)
# for i in a:
#     print(i)

#3
# n=int(input())
# class Custom:
#     def __init__(self,n):
#         #self.n=n
#         self.num=0
#         self.count=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         if self.count<=n:
#             value=self.num
#             self.num+=2
#             self.count+=1
#             return value
#         else:
#             raise StopIteration
# a=Custom(n)
# for i in a:
#    print(i)

#4
# n=list(map(int,input().split()))
# class Custom:
#     def __init__(self,n):
#         self.n=n
#         self.num=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.num<=len(n):
#             value=self.num
#             self.num+=1
#             if value%2==0:
#                 return value
#         raise StopIteration
# a=Custom(n)
# for i in a:
#     print(i,end=" ")

#5
# n=list(map(int,input().split()))
# class Custom:
#     def __init__(self,n):
#         self.n=n
#         self.num=1
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.num<=len(n)-1:
#             value=self.n[self.num]
#             self.num+=1
#             if value%2==1:
#                 return value
#         raise StopIteration
# a=Custom(n)
# for i in a:
#     print(i,end=" ")
#
# # #6
# n=list(map(int,input().split()))
# class Custom:
#     def __init__(self,n):
#         self.n=n
#         self.num=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.num<len(n):
#             value=self.n[self.num]
#             self.num+=1
#             if value>0:
#                 return value
#         raise StopIteration
# a=Custom(n)
# for i in a:
#      print(i,end=" ")

#7
# n=input()
# class Custom:
#     def __init__(self,n):
#         self.n=n
#         self.num=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.num<len(n):
#             value=self.n[self.num]
#             self.num+=1
#             return value
#         else:
#             raise StopIteration
# a=Custom(n)
# for i in a:
#      print(i,end=" ")

#8
n=input()
class Custom:
    def __init__(self,n):
        self.n=n
        self.num=len(n)-1
    def __iter__(self):
        return self
    def __next__(self):
        while self.num>=0:
            value=self.n[self.num]
            self.num-=1
            return value
        else:
            raise StopIteration
a=Custom(n)
for i in a:
     print(i,end=" ")
#
#9
# n=input()
# class Custom:
#     def __init__(self,n):
#         self.n=n
#         self.chr=0
#     def __iter__(self):
#         return self
#     def __next__(self):
#         while self.chr<=len(n)-1:
#             value=self.n[self.chr]
#             self.chr+=1
#             if value in "aeiou":
#                 return value
#         raise StopIteration
# a=Custom(n)
# for i in a:
#     print(i)


