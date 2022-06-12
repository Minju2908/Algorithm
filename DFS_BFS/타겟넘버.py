from itertools import product


def create_graph(numbers):
    graph = {}
    for i in range(len(numbers)):
        graph[i] = [numbers[i], -numbers[i]]

    return list(graph.values())


def solution(numbers, target):
    g = create_graph(numbers)
    a = list(product(*g))
    cnt = 0
    for i in a:
        if target == sum(i):
            cnt += 1

    return cnt