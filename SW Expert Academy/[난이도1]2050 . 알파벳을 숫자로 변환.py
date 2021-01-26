

T = input().split('')
result = 0
base = ord('A')
for i in T:
    num = ord(i)-base + 1
    result += ' '+str(num)

