def solution(number, k):
    answer = ''
    number = list(number)
    pos = len(number)-k
    _max = max(number[0:pos-1])
    answer = "".join([str(i) for i in number])
    return answer

number = "87654321"
k = 4
a = solution(number, k)
print(a)
