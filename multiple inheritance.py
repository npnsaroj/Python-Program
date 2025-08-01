class A:
    def show(self):
        print("Class A")

class B:
    def display(self):
        print("Class B")

class C(A, B):  # Inherits from both A and B
    def extra(self):
        print("Class C")

obj = C()
obj.show()     # From class A
obj.display()  # From class B
obj.extra()



class A:
    def show(self):
        print("A")

class B(A):
    def show(self):
        print("B")

class C(A):
    def show(self):
        print("C")

class D(B, C): 
    pass

obj = D()
obj.show()