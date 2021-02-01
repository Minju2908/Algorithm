T = int(input())

for test_case in range(1, T+1):
    N = int(input())
    s = ''
    for i in range(N):
        AL, cnt = map(str, input().split())
        s = s + AL * int(cnt)
    print(f'#{test_case}')
    for i in s:
        if len(s) > 10:
            print(f'{s[:10]}')
            s = s[10:]
        else:
            print(f'{s}')
            break


