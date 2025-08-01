def my_generator(n):
    value = 0
    while value < n:
        yield value
        value += 1
for value in my_generator(3):
    print(value)



    '''even numbers using generator'''
def even_numbers(n):
    for i in range(n):
        if i % 2 == 0:
            yield i

for num in even_numbers(10):
    print(num)
