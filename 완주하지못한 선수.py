from collections import Counter
def solution(participant, completion):
    answer = ''
    par_counter = Counter(participant)
    com_counter = Counter(completion)

    for per in participant:
        if par_counter[per]!= com_counter[per]:
            answer = per
    return answer

participate = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
completion = ['josipa', 'filipa', 'marina', 'nikola']

