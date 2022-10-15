

# col 길이는 1000이하
# 0<= j <=1, N-2<j<N-1
# i<255

for T in range(10):
    N = int(input())                        # 건물의 수(왼쪽 오른쪽 각 2개 포함)
    H = list(map(int, input().split(' ')))  # 건물의 높이(총합=세대의 수)
    highest = max(H)

    building = [[0]*highest for i in range(N)]

    for i in range(0, N):
        if i <= 1 or i >= N-2:
            continue
        else:
            for j in range(H[i]):
                building[i][j] = 1

    cnt = 0
    for b in range(N):
        if b <= 1 or b >= N-2:
            continue
        for h in range(H[b]):
            if building[b-1][h] + building[b-2][h] + building[b+1][h] + building[b+2][h] == 0:
                cnt += 1

    print(f'#{T+1} {cnt}')


