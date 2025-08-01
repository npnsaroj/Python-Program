def add(*num):
    sum=0
    for n in num:
     sum=sum+n
    print(sum)

add(2,3)
add(2,3,4)


def add(**num):
   sum=0
   for k,v in num.items():
      sum=sum+v
   print(sum)

add(a=2,b=3)
add(a=4,b=5,c=7)