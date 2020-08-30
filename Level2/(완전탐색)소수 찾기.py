from itertools import permutations
from math import sqrt

def find(num):
    for i in range(2,sqrt(num)):
        back = num-1
        if num%i==0 or num%back == 0:
            return 0
        else:
            back-=1
    return 1


def solution(numbers):
    answer = 0
    com = []
    numbers = list(numbers)

    for i in range(1,len(numbers)+1):
        a = list(permutations(numbers, i))
        com.append(a)

    com = [int("".join(j)) for i in com for j in i if int("".join(j))>=2]
    com = set(com)

    for num in com:
        result = find(num)
        if result == 1:
            answer+=1
    return answer

