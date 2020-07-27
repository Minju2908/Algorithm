def solution(s):
    answer = ''
    s = s.upper()
    index = 0
    for i in s:
        if i != ' ':
            index+=1
            if index % 2 != 0:
                answer+=i
            else:
                answer+=i.lower()
        else:
            index = 0
            answer+=' '
    return answer

