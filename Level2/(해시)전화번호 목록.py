def solution(phone_book):
    for i in phone_book:
        for j in phone_book:
            if i == j[0:len(i)] and i!=j:
                return False
    return True
