

T = int(input())
for test_case in range(1, T + 1):
    s = input()
    result = 1
    strs = [c for c in s]
    if strs.pop(0) != strs.pop():
        result = 0
    print(f'#{test_case} {result}')

