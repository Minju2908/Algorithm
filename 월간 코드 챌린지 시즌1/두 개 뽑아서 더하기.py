def solution(numbers):
    answer =[]
    for i in range(len(numbers)):
        for idx in numbers:
            if i!=numbers.index(idx):
                answer.append(numbers[i]+idx)

    return sorted(list(answer))

a= [2,1,3,4,1]
solution(a)