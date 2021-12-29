#optimised lst for easy insertion & deletion
from collections import deque
q=['r','u','s','t','a','m']
a=deque(q)
print(a)
a.appendleft('rustam') #as append adds val to right end this is used to add to left end
print(a)
a.popleft() #as pop removes val from right end this is uesd to remove from left end
print(a)



