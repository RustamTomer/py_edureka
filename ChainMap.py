# a dict like class for creating single view (list) of multiple mappings (dictionaries)
from collections import ChainMap
a={
    "name":"Rustam",
    "section":"X1"
}
b={
    "rollno":677,
    "attendance":100
}
a1=ChainMap(a,b)
print(a1)


