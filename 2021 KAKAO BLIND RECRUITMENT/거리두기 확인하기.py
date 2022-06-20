import numpy as np


def cal_dis(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def sol(P):
    places = np.array([list(place) for place in P])
    idx = np.where(places == 'P')
    row = idx[0]
    col = idx[1]
    num = len(row)
    answer = 1
    if num == 0:
        return 1
    else:
        for l in range(num):
            std = (row[l], col[l])
            for r_p, c_p in zip(row[l+1:], col[l+1:]):
                com = (r_p, c_p)
                if cal_dis(std, com) > 2:
                    continue
                else:
                    if std[0] == com[0]: # row
                        min_v = min(std[1], com[1])
                        max_v = max(std[1], com[1])
                        if 'X' not in list(places[std[0],min_v:max_v+1]):
                            return 0

                    elif std[1] == com[1]: # col
                        min_v = min(std[0], com[0])
                        max_v = max(std[0], com[0])
                        if 'X' not in list(places[min_v:max_v+1,std[1]]):
                            return 0

                    else:
                        if std[1] < com[1]:
                            if places[std[0]][std[1]+1] != 'X' or places[std[0]+1][std[1]] != 'X':
                                return 0
                        else:
                            if places[std[0]][std[1] - 1] != 'X' or places[std[0] + 1][std[1]] != 'X':
                                return 0

    return answer

def solution(places):
    answer = []
    for i in places:
        answer.append(sol(i))
    return answer

places = [["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPOX", "OXXOP", "PXPOX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]
print(solution(places))