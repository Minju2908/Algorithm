from _collections import deque

def solution(progresses, speeds):
    day = deque()
    for i in range(len(speeds)):
        day.append(0)
    answer = []

    for idx in range(len(progresses)):
        while 1:
            if progresses[idx]<100:         # 작업진도<100
                day[idx]+=1                 # 작업기간 +1
                progresses[idx]+=speeds[idx]
            else:
                break
    while day:
        val = day.popleft()
        cnt = 1
        for i in range(len(day)):
            num = day.popleft()
            if val >= num:
                cnt+=1
            else:
                day.appendleft(num)
                break
        answer.append(cnt)
    return answer
