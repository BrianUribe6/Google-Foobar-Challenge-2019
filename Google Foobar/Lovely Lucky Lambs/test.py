from math import sqrt, log

def fib(n):
    a, b = 1, 1
    i = 1
    n -= a 
    while b <= n:
        n -= b
        a,b = b, a + b
        i += 1
    return i

def solution(total_lambs):
    generous = fib(total_lambs)
    stingy = int(log(total_lambs + 1, 2))
    return abs(generous - stingy)

print(solution(10))

