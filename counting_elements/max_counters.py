'''
A Codility Lesson
MaxCounters

https://app.codility.com/programmers/lessons/4-counting_elements/max_counters/
'''

def solution_1(N, A):
    counters = [0]*N
    maximum_value = 0
    for index in range(0, len(A)):
        if A[index] <= N:
            counters[A[index] - 1] += 1
            if counters[A[index] - 1] > maximum_value:
                maximum_value = counters[A[index] - 1]
        else:
            counters = [maximum_value]*N

    return counters
        
def solution_2(N, A):
    counters = [0]*N
    for index in range(0, len(A)):
        if A[index] <= N:
            counters[A[index] - 1] += 1
        else:
            counters = [max(counters)]*N

    return counters

def solution_3(N, A):
    counters = [0]*N
    maximum_value = 0
    for each in A:
        if each <= N:
            counters[each - 1] += 1
            if counters[each - 1] > maximum_value:
                maximum_value = counters[each - 1]
        else:
            counters = [maximum_value]*N

    return counters


# From https://codesays.com/2014/solution-to-max-counters-by-codility/
def solution_4(N, A):
    result = [0]*N    # The list to be returned
    max_counter = 0   # The used value in previous max_counter command
    current_max = 0   # The current maximum value of any counter
    for command in A:
        if 1 <= command <= N:
            # increase(X) command
            if max_counter > result[command-1]:
                # lazy write
                result[command-1] = max_counter
            result[command-1] += 1
            if current_max < result[command-1]:
                current_max = result[command-1]
        else:
            # max_counter command
            # just record the current maximum value for later write
            max_counter = current_max
    for index in range(0,N):
        if result[index] < max_counter:
            # This element has never been used/updated after previous
            #     max_counter command
            result[index] = max_counter
    return result