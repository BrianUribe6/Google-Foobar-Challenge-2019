from fractions import Fraction
from functools import reduce


def transposeMatrix(m):
    return map(list,zip(*m))


def getMatrixMinor(m, i, j):
    return [row[:j] + row[j+1:] for row in (m[:i]+m[i+1:])]


def getMatrixDeternminant(m):
    #base case for 2x2 matrix
    if len(m) == 2:
        return m[0][0]*m[1][1]-m[0][1]*m[1][0]

    determinant = 0
    for c in range(len(m)):
        determinant += ((-1)**c)*m[0][c]*getMatrixDeternminant(getMatrixMinor(m,0,c))
    return determinant


def getMatrixInverse(m):
    #Checking if matrix is square:
    if len(m) != len(m[0]):
        raise ValueError("m must be a square matrix")
    determinant = getMatrixDeternminant(m)

    #special case for 2x2 matrix:
    if len(m) == 2:
        return [[m[1][1]/determinant, -1*m[0][1]/determinant],
                [-1*m[1][0]/determinant, m[0][0]/determinant]]

    #find matrix of cofactors
    cofactors = []
    for r in range(len(m)):
        cofactorRow = []
        for c in range(len(m)):
            minor = getMatrixMinor(m,r,c)
            cofactorRow.append(((-1)**(r+c)) * getMatrixDeternminant(minor))
        cofactors.append(cofactorRow)
    cofactors = list(transposeMatrix(cofactors))
    for r in range(len(cofactors)):
        for c in range(len(cofactors)):
            cofactors[r][c] = cofactors[r][c]/determinant
    return cofactors


def subtract(a, b):
    result = []
    for i in range(len(a)):
        #element wise subtraction for each row
        result.append(list(map(lambda a,b: a - b, a[i], b[i])))
    return result


def dot(X, Y):
    colX_size = len(X[0])
    rowY_size = len(Y)

    if colX_size != rowY_size:
        print(colX_size, rowY_size)
        raise ValueError("Number of columns A does not match number of rows B")

    return [[sum(a*b for a,b in zip(X_row,Y_col)) for Y_col in zip(*Y)] for X_row in X]
            

def eye(size):
    """Returns Identity matrix given a size"""
    return [[1 if i == j else 0 for j in range(size)] for i in range(size)]


def zeros(row, col):
    """Returns a matrix of zeroes given a row size and a column size"""
    return [[0 for _ in range(col)]for _ in range(row)]


def make_fraction(m):
    """Converts a given matrix of numbers to fractions with a denominator equal to the sum of an entire row"""
    size = len(m)

    for i in range(size):
        row_denom = sum(m[i])
        if row_denom == 0:
            row_denom = 1
        for j in range(size):
            m[i][j] = Fraction(m[i][j], row_denom).limit_denominator()

def gcd(a, b):
    """Calculate the Greatest Common Divisor of a and b.

    Unless b==0, the result will have the same sign as b (so that when
    b is divided by it, the result comes out positive).
    """
    while b:
        a, b = b, a%b
    return a


def solution(m):
    """Implements markov chains to return an array of ints for each 
    terminal state giving the exact probabilities of each terminal state, 
    represented as the numerator for each state, then the denominator for 
    all of them at the end and in simplest form.
    """ 
    
    # Special case for a 1x1 chain
    if len(m) == 1:
        return [1, 1]   
    
    make_fraction(m)
    non_terminal = {}

    # counting terminal states 
    index = 0
    for i in m:
        for j in i:
            # state is not terminal because there is some probability of achieving it 
            if j!= 0:
                # adding to dictionary to keep track of non-terminal states
                non_terminal[index] = i 
                break
        index += 1
    Q = []
    R = []
    # Iterating over each key, which happens to be the index of a non-terminal state
    for key in non_terminal:
        # containers for each row corresponding to either Q matrix or R matrix 
        curr_row_Q = []
        curr_row_R = [] 
        for curr_state in range(len(non_terminal[key])):
            if curr_state in non_terminal:
                curr_row_Q.append(non_terminal[key][curr_state])
            # is Terminal
            else: 
                curr_row_R.append(non_terminal[key][curr_state])
        Q.append(curr_row_Q)
        R.append(curr_row_R)
    
    I = eye(len(Q))
    # F = (I - Q)^-1
    F = getMatrixInverse(subtract(I, Q))
    FR = dot(F, R)[0]
    
    comm_denom = reduce(gcd, FR).denominator
    #converting to a list of numerators with the same common divisor, and appending the gcd at the end.
    for f in range(len(FR)):
        number = FR[f]
        FR[f] = int((comm_denom/ number.denominator * number.numerator))
    FR.append(comm_denom)
    
    return FR

print(list(map(list, zip(*[[1,2,3],[4,5,6],[7,8,9]]))))