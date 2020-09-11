def solution(s):
    answer = 0
    count = []
    if len(s)==1:
        return 1
    for i in range(1,(len(s)//2)+1):
        cnt = 1
        result = []
        strings = [s[idx:idx+i]for idx in range(0,len(s), i)]
        for j in range(len(strings)):
            if j!=len(strings)-1 and strings[j] == strings[j+1]:
                cnt+=1
            else:
                if cnt != 1:
                    result.append(str(cnt)+strings[j])
                    cnt = 1
                else:
                    result.append(strings[j])
        count.append(len(''.join(result)))
    return min(count)

s = "ababcdcdababcdcd"
s1 = "aabbaccc"
a = solution(s)
print(a)

