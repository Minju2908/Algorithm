def solution(num):
    answer = 0
    while answer<500:
        if num%2==0 and num!=1:
            num = num/2
        elif num!=1:
            num = (num*3)+1
        elif num == 1:
            break
        answer += 1

    if num != 1:
        return -1
    return answer
