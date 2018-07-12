# -*- coding: utf-8 -*-
L1 = ['Hello', 'World', 18, 'Apple', None]
L2 = [isinstance(x,str) for x in L1 if isinstance == True ]
print(L2)
if L2 == ['hello', 'world', 'apple']:
    print('success!')
else:
    print('fail')