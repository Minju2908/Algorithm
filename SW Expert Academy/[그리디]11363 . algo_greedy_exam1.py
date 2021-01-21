
T = int(input())

for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    result = 0
    while 1:
        result += (N % K)
        N = N // K
        result += 1
        if N < K:
            result += N-1
            break
    print(f'#{test_case} {result}')