def solution(number, k):
    answer = []
    for i in reversed(range(0,len(number)-k)):
        num = number[0:len(number)-i]
        answer.append(max(num))
        number = number[number.find(max(num))+1:]

    return ''.join(answer)

number = '4177252841'
k=4

a = solution(number, k)
print(a)
