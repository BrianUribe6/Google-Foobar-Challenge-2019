def solution(l):
    size = len(l)
    triplets = 0

    if size < 3:
        return 0  
    
    counter = [0] * size
    for x in range(size):
        for y in range(x+1, size):
            if l[y] % l[x] == 0:
                counter[y] += 1
                triplets += counter[x]      
    return triplets
