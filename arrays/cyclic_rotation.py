'''
A Codility Lesson
CyclicRotation

https://app.codility.com/programmers/lessons/2-arrays/cyclic_rotation/
'''

def solution(A, K):
    if len(A) == 0: # To handle empty list
        return A
    
    K = K % len(A)
    return A[-K:] + A[:-K]