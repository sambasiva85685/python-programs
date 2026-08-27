#1
def validate_postive(func):
    def wrappper(*args):
        for i in args:
            if i<0:
                print("Error Negative value is not a allowed")
                return None
            return func(*args)
    return wrappper
@validate_postive
def multiple(a,b):
    return a*b
print(multiple(5,6))
print(multiple(-6,4))


def cumculative_sum(list):
    sum=0
    for i in list:
        sum+=i
        yield sum
nums=[1,2,3,4]
for i in cumculative_sum(nums):
    print(i)
