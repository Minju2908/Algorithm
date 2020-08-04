def solution(strings, n):
    answer = []
    for i in strings:
        answer.append(i[n]+i)
    arr = sorted(answer)
    answer = list(i[1:] for i in arr)
    return answer

