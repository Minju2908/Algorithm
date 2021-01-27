def solution(number, k):
    answer = ''
    for i in reversed(range(0,len(number)-k)):
        num = number[0:len(number)-i]
        if '9' in num:
            M ='9'
        else:
            M = max(num)
            answer+=M
        number = number[number.find(M)+1:]
        if len(number) == i:
            return  ''.join(answer)+number
    return ''.join(answer)


number = '4177252841'
k=4

a = solution(number, k)
print(a)
