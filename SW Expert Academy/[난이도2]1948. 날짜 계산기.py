T = int(input())
for test_case in range(1, T + 1):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    result = 0
    m1, d1, m2, d2 = map(int, input().split())
    result = sum([days[i] for i in range(m1, m2)]) + (days[m1-1] - d1) - (days[m2-1] - d2) + 1
    print(f'#{test_case} {result}')