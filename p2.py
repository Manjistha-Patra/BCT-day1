#tuple to list and add data
#append
tup=(1,2,3,4)
a=list(tup)
a.append(5)
b=tuple(a)
print(b)


#extend
tup=(1,2,3,4)
a=list(tup)
a.extend([5,4])
b=tuple(a)
print(b)

#add two tuple
tup1=(11,22,33,44,55)
tup2=(66,77,88,99,00)
print(tup1+tup2)
#OR
tup=(1,2,3,4)+(5,6,7,8,9)
print(tup)