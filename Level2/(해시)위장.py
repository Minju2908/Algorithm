import collections
from itertools import permutations

def solution(clothes):
    answer = {}
    for i in clothes:
        if i[1] in answer:
            answer[i[1]].append(i[0])
        else:
            answer[i[1]]=[i[0]]
    for i in answer:
        answer[i] = len(answer[i])

    print(answer)
    return answer

clothes = [['yellow_hat', 'headgear'], ['blue_sunglasses', 'eyewear'], ['green_turban', 'headgear']]
solution(clothes)