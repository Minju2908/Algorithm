import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    while scoville:
        min = heapq.heappop(scoville)
        if not scoville:
            if min<K:
                return -1
        if min<K:
            sec_min = heapq.heappop(scoville)*2
            val = min+sec_min
            heapq.heappush(scoville, val)
            answer+=1
    return answer

