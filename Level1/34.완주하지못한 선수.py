from collections import Counter
def solution(participant, completion):
    answer = ''
    par_counter = Counter(participant)
    com_counter = Counter(completion)
    a = list(par_counter-com_counter)

    print(a[0])


participate = ['marina', 'josipa', 'nikola', 'vinko', 'filipa']
completion = ['josipa', 'filipa', 'marina', 'nikola']

solution(participate, completion)