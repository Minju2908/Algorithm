import re
def solution(new_id):
    new_id =  re.sub('[^a-z0-9-_.]', '', new_id.lower())
    while 1:
        if new_id[0] == '.' or new_id[-1] == '.':
            new_id = new_id.strip('.')
            while new_id.find('..') != -1:
                new_id = new_id.replace('..','.')
        if new_id == '':
            new_id = 'a'
        while len(new_id) < 3  or len(new_id) > 15:
            if len(new_id) < 3:
                new_id = new_id + new_id[-1]
            elif len(new_id) > 15:
                new_id = new_id[:15]
        if new_id[0] != '.' and new_id[-1] != '.' and len(new_id) >= 3  and len(new_id) <= 15:
            break
    return new_id