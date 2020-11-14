'''
A Codility Lesson

Binary Gap

https://app.codility.com/programmers/lessons/1-iterations/binary_gap/
'''

def solution(N):
    return len(max(bin(N)[2:].strip('0').strip('1').split('1')))


if __name__ == "__main__":
    number =  int(input("Enter a number: "))
    binary_gap = solution(number)
    print("Binary gap is", binary_gap)