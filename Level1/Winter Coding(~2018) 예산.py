def solution(d, budget):
    answer = []
    d.sort()
    cost = sum(d)
    if cost>budget:
        for i in d:
            answer.append(i)
            if sum(answer)>budget:
                return len(answer)-1
    return len(d)
