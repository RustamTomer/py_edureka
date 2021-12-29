from array import *

a=array('i',[1,2,3,4,5,6]) #no need to specify module while using this method
print(a)

#Accessing Elements
print(a[2])

##Basic array operations (arr is mutable)
print(len(a)) #length

a.append(7) #to add element at end
print(a)
a.extend([8,9,10,11]) #to add multiple elememts as end
print(a)
a.insert(1,12) #to insert element at a particular index
print(a)

a.pop()
print(a)
a.pop(1) #index specified
print(a)
a.pop(-1)
a.remove(1) #value specified
print(a)

#concatenation
b=array('i',[1,10])
c=array('i')
c=a+b
print(c)

#slicing (fetching particular vals frm arr)
print(c[0:4]) #final specified value isn't  included
print(c[0:-2])

#looping
#for
for x in c:
    print(x)

for x in c[0:4]:
    print(x)
#
print(c)
#while
p=0
while p<len(c):
    print(c[p])
    p=p+1 #p+=1
#
print(c)
#
t=0
while t<c[3]:
    print(c[t])
    t=t+1










