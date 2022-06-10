def solution(record):
    answer = []
    dict = {}
    users = []
    for user in record:
        if len(user.split(' ')) == 2:
            state, id = user.split(' ')
        else:
            state, id, name = user.split(' ')
            dict[id] = name

        if state != 'Change':
            users.append([state, id])

    for state, user in users:
        name = dict[user]
        if state == 'Enter':
            str = [name, "님이 들어왔습니다."]
            str = "".join(str)
        elif state == 'Leave':
            str = [name, "님이 나갔습니다."]
            str = "".join(str)

        answer.append(str)

    return answer


record = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(record))