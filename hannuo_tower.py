# -*- coding: utf-8 -*-
def move(n, a, b, c):
    if n == 1:
        print(a, '-->', c)
    else:
        move(n-1, a, c, b) #先把第n-1个盘子移到B
        move(1, a, b, c) #把剩下的那一个n移到C，
        move(n-1, b, a, c) #再把B上的第n-1移到C
move(3, 'A', 'B', 'C')