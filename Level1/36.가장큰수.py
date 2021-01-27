def solution(numbers):
    __sort = []
    answer = ''
    num_sort = sorted(numbers, key=lambda x: x//10**(len(str(x))-1), reverse=True)
    for num in num_sort:
        if len(str(num)) == 1:
            num = [str(num)*3,num]
        elif len(str(num)) == 2:
            num = [str(num//10)+str(num%10)+str(num//10), num]
        else:
            num = [str(num), num]
        __sort.append(num)
    __sort = sorted(__sort, key=lambda x: int(x[0]), reverse=True)
    for i in range(len(__sort)):
        try:
            if __sort[i][1]<__sort[i+1][1] and __sort[i][0]==__sort[i+1][0]:
                temp = __sort[i+1][1]
                temp2 = __sort[i][1]
                __sort[i+1][1] = temp2
                __sort[i][1] = temp
        except:
            pass
    return ''.join(str(i[1]) for i in __sort)

numbers = [6,10,2]

a= solution(numbers)
print(a)
