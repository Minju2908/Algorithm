
N = int(input())
n = '369'

for num in range(1, N+1):
    cnt = 0
    for i in str(num):
        a = n.find(i)
        if a != -1:
            cnt+=1
    if cnt != 0:
        print('-'*cnt, end=' ')
    else:
        print(num, end=' ')


