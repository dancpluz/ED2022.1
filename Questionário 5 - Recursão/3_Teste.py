def Fib(n):
    global count
    count += 1
    if n == 0:
        return n
    elif n == 1:
        return n
    else:
        return(Fib(n-1) + Fib(n-2))

count = 0
n = int(input())
print(f'Fib({n}) = {Fib(n)} ({count} chamadas)')
