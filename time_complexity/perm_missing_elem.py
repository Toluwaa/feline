'''
A Codility Lesson
PermMisssinElem

https://app.codility.com/programmers/lessons/3-time_complexity/perm_missing_elem/
'''
def solution(A):
    length = len(A)
    digger = 0

    for index in range(0, length):
        digger = digger ^ A[index] ^ (index+1)
        
    return digger ^ (length+1)
