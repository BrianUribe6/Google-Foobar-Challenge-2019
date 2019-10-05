
def fib(n):
    a, b = 0, 1
    i = 0
    while i <= n:
        i += 1
        a, b = b, a + b
    return b

for i in range(10):
    print(fib(i))