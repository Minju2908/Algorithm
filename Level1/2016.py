def solution(a, b):
    answer = ''
    day = b
    month = [31,29,31,30,31,30,31,31,30,31,30,31]
    days = ["FRI", "SAT","SUN","MON","TUE","WED","THU"]
    for i in month[:a-1]:
        day+=i
    answer = days[(day%7)-1]
    return answer

