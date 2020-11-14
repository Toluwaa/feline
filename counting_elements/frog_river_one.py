'''
A Codility Lesson
FrogRiverOne

https://app.codility.com/programmers/lessons/4-counting_elements/frog_river_one/
'''

def solution_1(X, A):
    position = 0 # Number of positions filled
    index = 0
    while index < len(A):
        if A[index] not in A[:index]:
            position += 1
            if position == X:
                return index
        
        index += 1
    else:
        return -1

def solution_2(X, A):
    covered = [-1]*X # A list of all positions and the time covered
    uncovered = X # Number of positions not covered

    for index in range(0, len(A)):
        if covered[A[index] - 1] != -1:
            continue
        else:
            covered[A[index] - 1] = index
            uncovered -= 1
            if uncovered == 0:
                return index
    
    return -1
    