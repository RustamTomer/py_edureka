# dict subclass for counitng hashable objects
from collections import Counter
a=[1,1,4,5,7,6,4,5,3,9,8,4,5,8,3,2,2]
c=Counter(a)
print(c) # uses set symbol
#can be used for any iterable obj like tuple or set

#
print(list(c.elements())) #elements fn ; ascending order
print(c.most_common()) #most common fn ; sorted list according to intensity of count of an element
sub={4:1,9:1}
print(c.subtract(sub))
print(c.most_common())
print(c)



