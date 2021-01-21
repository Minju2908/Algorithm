

arr = input()
sum = ''
for i in range(len(arr)):
    sum += str(ord(arr[:1])-64) + ' '
    arr = arr[1:]
print(sum)