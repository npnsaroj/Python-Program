
add=lambda x,y:x+y 
print(add(10,20))

square=lambda x:x*x
print(square(5))

list1=[1,2,3,4,5]
list2=list(map(lambda x:x*x,list1))   #map function 
print(list2) 


numbers=[1,2,3,4,5,6,7,8,9]
even_numbers=list(filter(lambda x: x%2==0,numbers)) #filter function 
print(even_numbers)


