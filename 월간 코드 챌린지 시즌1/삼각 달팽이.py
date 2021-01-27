def solution(n):
    answer = []
    for i in range(1,n+1):
        num = i
        _temp=1
        print('-'*8)
        while num:
            print(num)
            temp = []
            temp.append(num)
            num-=1
        answer.append(temp)
    print(answer)
    return answer

solution(n=4)