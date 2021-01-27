from collections import Counter

def solution(n, words):
    answer = []
    count = Counter(word)
    for i in range(len(words)-1):
        last = len(words[i])
        if words[i][last-1]!=words[i+1][0]:
            person = i+1//n
            answer.append(person)
            answer.append((i + 1 // n) + 1)
            return answer

    for w, val in count.items():
        if val ==2:
            name = w
            break

    for i in range(len(words)):
        idx = 0
        if words[i]==name:
            idx = i
    person = idx + 1 // n
    answer.append(person)
    answer.append((i + 1 // n) + 1)
    return answer

    return [0,0]

word = ["tank", "kick", "know", "wheel", "land", "dream", "mother", "robot", "tank"]
n = 3

solution(n, word)