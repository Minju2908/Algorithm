from itertools import permutations

def solution(numbers):
    numbers = [str(i) for i in numbers]
    numbers = sorted(numbers, key= lambda x: x[0], reverse=True)
    first, last = 0, 0
    for i in range(len(numbers)-1):
        if numbers[i][0] ==numbers[i+1][0]:
            first=i
    mix = permutations(numbers, len(numbers))
    numbers = [int(''.join(list(i))) for i in set(numbers)]
    numbers.sort()

    return str(numbers[-1])

numbers = [3, 30, 34, 5, 9]
a = solution(numbers)
print(a)