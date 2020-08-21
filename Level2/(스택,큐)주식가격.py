def solution(prices):
    answer = [ 0 for i in prices]
    for i in range(len(prices)-1):
        for j in range(i+1,len(prices)):
            if prices[j]<prices[i]:
                answer[i]+=1
                break
            else:
                answer[i]+=1
    return answer
