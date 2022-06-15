def solution(w, h):
    answer = 1
    total = w * h
    if w == 1 or h == 1:
        return 0
    else:
        if w == h:
            answer -= w
            return answer
        else:
            if w % 2 != 0 and h % 2 != 0:
                min_v = min(w, h)
                answer = total - (min_v+1)*2 + 1
            else:
                if min(w, h) % 2 != 0:
                    min_val = min(w, h) + 1
                    answer = total - (min_val * 2)
                else:
                    min_val = min(w, h)
                    answer = total - (min_val * 2)

    return answer

val = solution(3, 5)

print(val)