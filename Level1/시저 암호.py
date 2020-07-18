from string import ascii_lowercase
from string import ascii_uppercase

def solution(s, n):
    answer = []
    alpha_up = list(ascii_uppercase)*2
    alpha_low = list(ascii_lowercase)*2
    for i in s:
        if i.isupper():
            alpha = alpha_up[ord(i)-65+n]
            answer.append(alpha)
        elif i.islower():
            alpha = alpha_low[ord(i) - 97 + n]
            answer.append(alpha)
        else:
            answer.append(" ")
    answer = "".join(answer)
    return answer


