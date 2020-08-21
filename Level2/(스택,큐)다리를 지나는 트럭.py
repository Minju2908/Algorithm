
def solution(bridge_length, weight, truck_weights):
    answer = 0
    waiting = [[i,0]for i in truck_weights]
    bridge = []
    while 1:
        if waiting:
            answer += 1
            truck = waiting.pop(0)
            if sum([i[0] for i in bridge])+truck[0] <= weight:
                bridge.append(truck)
                for i in bridge:
                    i[1] += 1
                for i in bridge:
                    if i[1] == bridge_length:
                        del bridge[0]
            else:
                waiting.insert(0,truck)
                for i in bridge:
                    i[1] += 1
                for i in bridge:
                    if i[1] == bridge_length:
                        del bridge[0]
        else:
            while bridge:
                answer+=1
                for i in bridge:
                    i[1] += 1
                for i in bridge:
                    if i[1] == bridge_length:
                        del bridge[0]
            break

    return answer+1

