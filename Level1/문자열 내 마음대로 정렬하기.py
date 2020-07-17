def solution(strings, n):
    answer = []
    answer= sorted(strings, key=lambda s:s[n])
    return answer


strings = ['sun', 'bud', 'car']
n = 1
print(solution(strings, n))