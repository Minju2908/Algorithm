def solution(arr, divisor):
    answer = []
    for i in range(len(arr)):
        if arr[i]%divisor==0:
            answer.append(arr[i])
    if not answer:
        answer.append(-1)
    else:
        answer.sort()
    return answer

print(solution(arr=[5, 9, 7, 10], divisor=5))