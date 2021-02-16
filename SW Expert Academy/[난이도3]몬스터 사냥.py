
T = int(input())
for test_case in range(1, T + 1):
    D, L, N = map(int, input().split())
    Sum = 0
    for i in range(N):
        Sum += D + D*(i*L*0.01)
    print(f'#{test_case} {int(Sum)}')