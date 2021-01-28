
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0]*N for i in range(N)]
    num, i, j = 1, 0, 0
    while num <= (N*N):
        for p in range(1, 5):
            if p == 3 or p == 4:
                a = -1
            else:
                a = 1
            while num <= (N*N):
                arr[i][j] = num
                if p == 1 or p == 3:
                    j += 1 * a
                else:
                    i += 1 * a
                num += 1
                if i < 0 or j < 0 or i >= N or j >= N or arr[i][j] != 0:
                    if p == 1 or p == 3:
                        i += 1*a
                        j -= 1*a
                    else:
                        i -= 1*a
                        j += -1*a
                    break
    print(f'#{test_case}')
    for i in arr:
        s = ''
        for j in i:
            s += str(j) + ' '
        print(s)