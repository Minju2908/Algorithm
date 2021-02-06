import operator
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    s = list(map(int, input().strip().split(' ')))
    a = {}
    for i in s:
        if i not in a:
            a[i] = 1
        else:
            a[i] = int(a[i]) + 1
    sdict = sorted(a.items(), key=operator.itemgetter(1), reverse=True)[0][0]
    print(f'#{test_case} {sdict}')