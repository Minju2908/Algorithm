# 조건1. 영문자로 된 글자 쌍만 유효,
# 조건2. 대소문자 구분 없음

from collections import Counter
import math

def my_solution(str1, str2):
    inter = 0
    union = 0
    str1 = [str1[i:i + 2].upper() for i in range(len(str1)) if str1[i:i+2].isalpha() and len(str1[i:i+2]) == 2]
    str2 = [str2[i:i + 2].upper() for i in range(len(str2)) if str2[i:i+2].isalpha() and len(str2[i:i+2]) == 2]

    if not str1 and not str2:
        answer = 1
    else:
        dict1 = Counter(str1)
        key1 = dict1.keys()

        dict2 = Counter(str2)
        key2 = dict2.keys()

        for k in key1:
            if not k in key2:
                union += dict1[k]

        for k in key2:
            if not k in key1:
                union += dict2[k]
            else:
                union += max(dict1[k], dict2[k])
                inter += min(dict1[k], dict2[k])

        answer = inter/union

    return math.trunc(answer * 65536)

def answer(str1, str2):
    str1 = [str1[i:i + 2].upper() for i in range(len(str1)) if str1[i:i+2].isalpha() and len(str1[i:i+2]) == 2]
    str2 = [str2[i:i + 2].upper() for i in range(len(str2)) if str2[i:i+2].isalpha() and len(str2[i:i+2]) == 2]

    # set 함수를 통해 list안에 중복원소를 제거할 수 있다.
    # '&' 기호는 같은 원소를 {} type으로 추출한다.
    # '|' 기호는 다른 원소를 {} type으로 추출한다.
    inter = set(str1) & set(str2)
    union = set(str1) | set(str2)

    if not union:
        answer = 1
    else:
        inter = sum([min(str1.count(i), str2.count(i)) for i in inter])
        union = sum([max(str1.count(i), str2.count(i)) for i in union])

        answer = inter/union

    return math.trunc(answer*65536)

print(answer('E=M*C^2', 'e=m*c^2'))
