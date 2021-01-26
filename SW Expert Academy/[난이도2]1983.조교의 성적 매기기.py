T = int(input())
grade = ['A+', 'A0', 'A-', 'B+', 'B0', 'B-', 'C+', 'C0', 'C-', 'D0']
for test_case in range(1, T + 1):
    N, k = map(int, input().split())
    sum = []
    for i in range(1, N+1):
        m, f, h = map(int, input().split())
        score = round(m*0.35 + f*0.45 + h*0.20, 4)
        if i == k:
            check = score
        sum.append(score)

    sum.sort(reverse=True)
    rank = sum.index(check)+1

    num = N // 10
    if (rank%num) == 0:
        result = grade[(rank//num)-1]
    else:
        result = grade[(rank//num)]

    print(f'#{test_case} {result}')