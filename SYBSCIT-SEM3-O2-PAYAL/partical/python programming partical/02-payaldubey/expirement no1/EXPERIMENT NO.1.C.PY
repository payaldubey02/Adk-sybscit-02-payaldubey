def fib(n):
    a=3
    b=5
    if n==1:
        print(a)
    else:
        print(a)
        print(b)
        for i in range(6,n):
            c=a+b
            a=b
            b=c
            print(c)
fib(30)
