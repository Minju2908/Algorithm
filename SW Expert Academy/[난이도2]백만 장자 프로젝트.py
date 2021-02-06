


T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    s = list(map(int, input().split(' ')))
    result = 0
    while len(s) > 1:
        max_i = s.index(max(s))
        if max_i != 0:
            arr = s[:max_i]
            result = result + (s[max_i]*len(arr)-sum(arr))
            s = s[max_i+1:]
        else:
            s.pop(0)
    print(f'#{test_case} {result}')


