def solution(numbers):
    arr = []
    _sort = sorted(numbers, key=lambda x: x // 10 ** (len(str(x)) - 1))
    for num in _sort:
        div = [i for i in str(num)]
        for i in range(4-len(str(num))):
            div.append(div[0])
        div.append(num)
        arr.append(div)
    __sort = sorted(arr, key=lambda x: (x[0],x[1],x[2],x[3]), reverse=True)
    answer = ''.join([str(i[4]) for i in __sort])
    return answer

number = [1,1,1,1,111,1000,1,10]
a =solution(number)
print(a)