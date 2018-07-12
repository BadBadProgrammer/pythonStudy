# -*- coding: utf-8 -*-
def trim(s):
    if (s[:1] == ' '):
        return trim(s[1:])
    elif (s[-1:] == ' '):
        return trim(s[:-1])
    else:
        return s

if trim('hello  ') != 'hello':
    print('failed')
elif trim('  hello') != 'hello':
    print('failed')
elif trim('  hello  ') != 'hello':
    print('failed')
elif trim('  hello  world  ') != 'hello  world':
    print('failed')
elif trim('') != '':
    print('failed')
elif trim('    ') != '':
    print('failed')
else:
    print('success')