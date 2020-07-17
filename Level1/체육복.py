def solution(n, lost, reserve):
    answer = 0
    for i in lost:
        if reserve.count(i) or reserve.count(i-1) or reserve.count(i+1):
            lost.remove(i)
            if reserve.count(i):
                reserve.remove(i)
            elif reserve.count(i+1):
                reserve.remove(i+1)
            else:
                reserve.remove(i-1)
    answer = n-len(lost)
    print(lost)
    return answer

print(solution(5, [1,2,3], [1,2,4,5]))
