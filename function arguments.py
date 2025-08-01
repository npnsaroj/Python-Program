#defualt Arguments 
# def add_numbers(a=10,b=20):
#     sum= a+b
#     print("Sum of a and b:",sum)

# add_numbers()
# add_numbers(a=5)

"*** keyword argument***"
def name(fname,lname):
    print("First name",fname)
    print('Last name:',lname)

name(fname="Messi",lname="lionel")

"***multiple value argument***"
def add_numbers(*num):
    sum=0
    for i in num:
        sum=sum+i
    print(sum)
    
add_numbers(2,4)
add_numbers(2,3,4)