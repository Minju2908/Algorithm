from itertools import product

def create_graph(numbers):
    graph = {}
    for i in range(len(numbers)):
        graph[i] = [numbers[i], -numbers[i]]
    return list(graph.values())

def solution(numbers, target):
    # g = create_graph(numbers)
    # 굳이 dictionary 만들 필요 없음.

    g = [(x, -x) for x in numbers]
    a = list(product(*g))
    cnt = 0
    for i in a:
        if target == sum(i):
            cnt += 1
    return cnt

print(solution([4,1,2,1],4))

