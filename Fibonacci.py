def fib(x):
    a,b,n = 1,0,0
    while n < x:
        a , b = b , a+b
        n = n+1
        print(b)
    
fib(6)