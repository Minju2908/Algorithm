
T = int(input())

for test_case in range(1, T + 1):
    s = input().strip()
    m = len(s)//2
    l = sum(map(int, s[:m]))
    r = sum(map(int, s[m:]))
    if l == r:
        print(f'#{test_case} LUCKY')
    else:
        print(f'#{test_case} READY')