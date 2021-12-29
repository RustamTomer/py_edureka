from collections import namedtuple
t=namedtuple('cars','suv, sports')
v=t._make(['urus', 'hyuara'])
print(v)
#previous method used instead of line 3
#v=t('urus', 'hyuara')
#curr line 3 method is called using list to put vals in tuple






