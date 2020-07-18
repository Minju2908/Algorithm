def solution(s):
    answer = False
    if len(s)==4 or len(s)==6:
        for i in s:
            if ord(i)>=48 and ord(i)<=57:
                answer = True
            else:
                return False
    else:
        return False
    return answer

# ========================
# 다른 풀이

def solution2(s):
    answer = True
    if len(s)==4 or len(s)==6:
        if not s.isdigit():
            return False
    else:
        return False
    return answer
