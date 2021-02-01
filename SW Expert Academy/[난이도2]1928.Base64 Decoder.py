import base64
T = int(input())

for test_case in range(1, T + 1):
    text = input()
    a = base64.b64decode(text).decode("UTF-8")
    print(f'#{test_case} {a}')
