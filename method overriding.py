class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def speak(self):
        super().speak()
        print("Dog barks")


a = Animal()
d = Dog()
a.speak()  
d.speak() 