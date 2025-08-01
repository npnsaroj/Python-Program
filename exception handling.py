a=int(input("enter numerator:"))
b=int(input("Enter denominator:"))
try:
    result=a/b
    print(result)
except ZeroDivisionError:
    print("Denominator can not be zero",)
else:
    print("No exception occurred")
finally:
    print("always executing")