def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

def series(n):
    if n == 0:
        return

    series(n-1)
    print(fib(n-1), end=" ")

n = int(input("enter number: "))
series(n)