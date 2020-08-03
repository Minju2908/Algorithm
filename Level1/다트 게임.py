import re

def solution(dartResult):
    numbers = re.findall(r'\d+', dartResult)
    index = 0
    for i in dartResult:
        if i == 'S':
            numbers[index] = int(numbers[index])**1
        elif i == 'D':
            numbers[index] = int(numbers[index])**2
        elif i =='T':
            numbers[index] = int(numbers[index])**3
        elif i == '*':
            index -= 1
            numbers[index] = int(numbers[index])*2
            if index!=0:
                numbers[index-1] = int(numbers[index-1])*2
        elif i =='#':
            index -= 1
            numbers[index] = int(numbers[index])*-1
        else:
            index-=1
            pass
        index+=1
    return sum(numbers)


