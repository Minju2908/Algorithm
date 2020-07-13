def solution(answers):
    answer = [0,0,0,0]
    max=0
    a = len(answers)
    p1 = [1, 2, 3, 4, 5]*(a//5+1)
    p2 = [2, 1, 2, 3, 2, 4, 2, 5]*(a//8+1)
    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]*(a//10+1)

    for i,j in zip(answers, p1):
        if i==j:
            answer[1]+=1
    for i,k in zip(answers, p2):
        if i==k:
            answer[2]+=1
    for i,l in zip(answers, p3):
        if i==l:
            answer[3]+=1
    for i in answer:
        if i>max:
            max=i
    return list(filter(lambda x: answer[x] == max, range(len(answer))))

