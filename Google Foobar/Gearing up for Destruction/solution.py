from fractions import Fraction
from random import sample, randint

test_cases = [sample(range(100), randint(0,20)) for i in range(1000)]

def answer(pegs):
    arrLength = len(pegs)
    if ((not pegs) or arrLength == 1):
        return [-1,-1]

    even = True if (arrLength % 2 == 0) else False
    sum = (- pegs[0] + pegs[arrLength - 1]) if even else (- pegs[0] - pegs[arrLength -1])

    if (arrLength > 2):
        for index in range(1, arrLength-1):
            sum += 2 * (-1)**(index+1) * pegs[index]

    FirstGearRadius = Fraction(2 * (float(sum)/3 if even else sum)).limit_denominator()
    #now that we have the radius of the first gear, we should again check the input array of pegs to verify that
    #the pegs radius' is atleast 1.

    currentRadius = FirstGearRadius
    for index in range(0, arrLength-2):
        CenterDistance = pegs[index+1] - pegs[index]
        NextRadius = CenterDistance - currentRadius
        if (currentRadius < 1 or NextRadius < 1):
            return [-1,-1]
        else:
            currentRadius = NextRadius 

    return [FirstGearRadius.numerator, FirstGearRadius.denominator]

def solution(pegs):
    size = len(pegs)
    even = False
    if size <2:
        return [-1, -1]
    if size % 2 == 0:
        even = True
        sum = -pegs[0] + pegs[-1]
    elif size %2 != 0:
        sum = sum = -pegs[0] - pegs[-1]
    
    if size > 2:
        for i in range(1, size-1):
            sum += 2 * (-1)**(i+1) * pegs[i]
    
    #Radius of first gear
    if even:
        r0 = Fraction(2.0 * sum/3).limit_denominator()
    else:
        r0 = Fraction(2.0 * sum).limit_denominator()
    
    curr_rad = r0
    for j in range(size-2):
        #distance between pegs
        d = pegs[j+1] - pegs[j]
        next_rad = d - curr_rad
        if curr_rad <1 or next_rad <1:
            return [-1, -1]
        else:
            curr_rad = next_rad
    return [r0.numerator, r0.denominator]
    
print(answer([25, 67, 79, 59])) 
print(solution([25, 67, 79, 59]))
