def solution(bridge_length, weight, truck_weights):
    answer = 0
    waiting = [[i, 0]for i in truck_weights]
    bridge = []
    while waiting:
        truck = waiting.pop(0)
        if sum([i[1] for i in bridge])+truck[0] <= weight:
            bridge.append(truck)
        else:
            pass

        for i in bridge:
            i[1]+=1
            if i[1]>bridge_length:
                bridge.pop(0)

    return answer



bridge_length = 2
weight = 10
truck_weights = [7,4,5,6]

a = solution(bridge_length, weight, truck_weights)
print(a)
