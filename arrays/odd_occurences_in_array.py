'''
A Codility Lesson
OddOccurencesInArray

https://app.codility.com/programmers/lessons/2-arrays/odd_occurrences_in_array/
'''

def solution(A):
    digger = 0
    for each in A:
        digger ^= each
    
    return digger