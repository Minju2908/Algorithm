# 조건1. 영문자로 된 글자 쌍만 유효,
# 조건2. 대소문자 구분 없음

from collections import Counter
import math
def solution(str1, str2):
    # 집합 원소 카운트 -> 집합 or 다중 집합
    # 합집합 / 교집합 생성
    # 계산
    answer = 0

    inter = []
    union = []
    str1 = [str1[i:i + 2].upper() for i in range(len(str1)) if str1[i:i+2].isalpha() and len(str1[i:i+2]) == 2]
    str2 = [str2[i:i + 2].upper() for i in range(len(str2)) if str2[i:i+2].isalpha() and len(str2[i:i+2]) == 2]

    if not str1 and not str2:
        return 1 * 65536

    dict1 = Counter(str1)
    key1 = dict1.keys()

    dict2 = Counter(str2)
    key2 = dict2.keys()

    for str in key2:
        if str not in key1:
            union.extend([str]*dict2[str])
        elif str in key1:

            a = dict1[str]
            b = dict2[str]

            union += max(a, b)
            inter += min(a, b)

            if a > b:
                dict1[str] -= dict2[str]
            else:
                del(dict1[str])

    union += sum(dict1.values())
    answer = math.trunc((inter/union) * 65536)
    return answer

print(solution('aa1+aa2', 'AAAA12'))
print((2/3)*65536)