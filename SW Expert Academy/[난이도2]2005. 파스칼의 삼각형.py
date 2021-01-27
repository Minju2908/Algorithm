
T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    arr = [[0]*10 for i in range(10)]
    result = ''

    for i in range(0,N):
        arr [i][0] = 1
        for j in range(1, i):
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j]
        arr[i][i] = 1
        for j in arr[i]:
            if j != 0:
                print(j, end=' ')
        print('')
