'''
A Codility  Lesson
FROGJMP

https://app.codility.com/programmers/lessons/3-time_complexity/frog_jmp/
'''
import math

def solution_1(X, Y, D):
    jump = math.ceil((Y - X) / D)
    return jump

def solution_2(X, Y, D):
    jump = (Y-X)//D if (Y-X) % D == 0 else (Y-X)//D + 1
    return jump