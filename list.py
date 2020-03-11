#delete an element by index

l=[1,2,3,4,5]
del l[2]
print(l)

l.append(16)
print(l)

l.remove(16)
print(l)

m=[16,17,18,19]
l.extend(m)
print(l)

l[:]=[]
print(l)

l=[i for i in range(10)]
print(l)

#print(l[1:3])
#print(l.clear())
#print(l)

l=[1,2,3,4,5,6]
m=l[-1:-4]
print(m)








