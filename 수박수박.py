def solution(n):
    answer = ''
    str = '수박'
    if n%2==0:
        answer = str*(n/2)
    else:
        answer = str*(n//2) + str[0]
    return answer



