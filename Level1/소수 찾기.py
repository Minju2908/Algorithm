def solution(n):
    answer = list(range(2,n+1))
    for i in answer[1:n]:
        for j in range(2,i):
            if i%j==0:
                answer.remove(i)
                break
    return len(answer)



print(solution(10))
print(solution(100))
