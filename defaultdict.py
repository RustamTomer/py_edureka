# a dict subclass which calls a factory func to supply missing vals
from collections import defaultdict
d = defaultdict(int)

d[1] = 'spacex'
d[2] = 'tesla'
print(d)
print(d[3]) #no keyerror is thrown





