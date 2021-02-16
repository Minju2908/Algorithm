import sys
sys.stdin = open("input.txt", "r")
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0]*N for i in range(N)]
    for i in range(N):
        arr[i] = list(input())
    end = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 'o':
                ch = [1, 1, 1, 1]
                for t in range(0, 5):
                    if j+t < N and arr[i][j+t] == 'o':
                        ch[0] += 1
                    elif i+t < N and arr[i+t][j] == 'o':
                        ch[1] += 1
                    elif j+t < N and i+t < N and arr[i+t][j+t] == 'o':
                        ch[2] += 1
                    elif i+t < N and arr[i+t][j+(t*-1)] == 'o':
                        ch[3] += 1
                if 5 in ch:
                    print(f'#{test_case} YES')
                    end = 1
                    break

        if end == 1:
            break
    if end == 0:
        print(f'#{test_case} NO')

