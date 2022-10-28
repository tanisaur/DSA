'''Given: 
    An array of non-negative digits that represent a decimal integer
   Problem:
    Add one to the integer. Assume the solution will still work if implemented 
    in a language with finite-precision arithmetic
'''
A1 = [1, 4, 9]
A2 = [9, 9, 9]

s = ''.join(map(str, A1))
print(int(s) + 1)


def plus_one(A):
    #add 1 to the rightmost digit
    A[-1] += 1
    #propogate carry throughout the array
    for i in reversed(range(1, len(A))):
        if A[i] != 10:
            break
        A[i] = 0
        A[i-1] += 1
    #case if index is 10    
    if A[0] == 10:
        A[0] = 1
        A.append(0)
    return A


print(plus_one(A1))
print(plus_one(A2))