
T = int(input())

for test_case in range(1, T + 1):
    a = input()
    result = 0
    year = int(a[:4])

    mon  = int(a[4:6])
    day  = int(a[6:])
    if (mon > 12) or (mon < 1):
        result = -1
    elif mon == 2:
        if day < 1 or day > 28:
            result = -1
    elif mon == 4 or mon == 6 or mon == 9 or mon == 11:
        if day < 1 or day > 30:
            result = -1
    else:
        if day < 1 or day > 31:
            result = -1
    if result != -1:
        result = str(year).zfill(4)+'/' + str(mon).zfill(2) + '/' + str(day).zfill(2)
    print(f'#{test_case} {result}')
