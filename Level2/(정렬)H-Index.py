from collections import Counter

def solution(citations):
    citations.sort()
    for i in range(len(citations)):
        cnt = 0
        use = citations[i]
        for i in range(i+1, len(citations)):
            if cnt<use:
                cnt+=1
            else:
                break
        if cnt == use:
            print(use)
            return use


solution(citations=[3, 0, 6, 1, 5])
