def decorator_function(func): #function that takes another function as a input and modifies behavior 
    def wrapper_function():
        print("I got decorated")
        func()
    return wrapper_function

@decorator_function
def ordinary():
    print('i am ordinary ')
ordinary()


def smart_divide(func):   # decorating function with parameters
    def inner(a,b):
        print("I am going to devide",a,"and",b)
        return func(a,b)
    return inner
@smart_divide
def divide(a,b):
    print(a/b)

divide(5,4)