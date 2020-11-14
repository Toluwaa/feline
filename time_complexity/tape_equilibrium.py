'''
A Codility Lesson
TapeEquilibrium

https://app.codility.com/programmers/lessons/3-time_complexity/tape_equilibrium/
'''
def solution(A):
    top = A[0]
    bottom = sum(A[1:])

    minimum = abs(top - bottom) # Minimum difference
    for index in range(1, len(A)-1):
        top += A[index]
        bottom -= A[index]

        diff = abs(top - bottom)
        if diff < minimum:
            minimum = diff
            
     return minimum
