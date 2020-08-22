def solution(number, k):
    answer = ''
    number = list(number)
    while k > 0:
        for i in range(len(number) - 1):
            if number[i] < number[i + 1]:
                number.remove(number[i])
                k -= 1
                break
    answer = "".join([str(i) for i in number])
    return answer


