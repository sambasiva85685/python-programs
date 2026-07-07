 #1
def login(func):
    def inner():
        print("Checking login")
        func()
    return inner
def admin(func):
    def inner():
        print("Checking admin permission")
        func()
    return inner
@login
@admin
def delete_record():
    print("Record deleted")
delete_record()


#2
def log(func):
    def inner(a,b):
        print("Before calculation")
        func(a,b)
        print("After calculation")
    return inner
def validate(func):
    def inner(a,b):
        print("Checking inputs")
        func(a,b)
    return inner
@log
@validate
def add(a,b):
    print(a+b)
add(2,5)

#3
def auth_required(func):
    def inner():
        print("checking user authencation")
        func()
    return inner
def payment_required(func):
    def inner():
        print("checkingpaymentstatus")
        func()
    return inner
@auth_required
@payment_required
def download_course():
    print("course downloaded")
download_course()