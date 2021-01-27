chages = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
T = int(input())
for test_case in range(1, T + 1):
    total  = int(input())
    print(f'#{test_case}')
    for i in chages:
        print(str(total // i), end=' ')
        total = total - (total //i)*i
    print()