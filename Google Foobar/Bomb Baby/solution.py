def solution(M, F):
    a,b = max(int(M),int(F)), min(int(M),int(F))
    i = -1
    while b >0:
        i += a /b
        a, b = b, a%b
        if a>1 and b ==0:
            return "impossible"
    return str(i)
print(solution("4", "7"))