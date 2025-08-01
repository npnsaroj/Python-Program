a=[10,20,30,40]  # list:ordered, allows duplicates, mutable
print (a)
print(a[3]) 
print(a[1:3])
a.append(50)
print(a) 

'''tuples'''
players=("Messi","Ronaldo","Neymar","Suarez") # ordered, immutable,allows duplicates
print(players)
print(players.count('Messi'))
print(players[:-2])

'''set'''
num={1,2,3,4,5,6}
print(num)
num.add(10)
print(num)
empty_set=set()

'''dicitionary'''
capitals={'Nepal':'Kathmandu','India':'New delhi','Japan':'Tokyo'}
print(capitals)
capitals['Bhutan']='Thimpu'
del capitals['India']
print(capitals)
print(len(capitals))
print(capitals.keys())
print(capitals.items())
print(capitals.clear())