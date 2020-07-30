def solution(n, m):
    answer = []
    n_1 = []                #약수
    m_1 = []                #약수
    for i in range(1,int(n)+1):
        if n%i==0:
           n_1.append(i)

    for j in range(1,int(m)+1):
        if m%j==0:
            m_1.append(j)
    for x in n_1[::-1]:
        if len(answer)<1:
            for y in m_1:
                if x==y:
                    answer.append(x)
                    break
        else:
            break
    answer.append(int(answer[0] * m/answer[0] * n/answer[0]))
    return answer

a = solution(126,5000)

def gcdlcm(a, b):
    c, d = max(a, b), min(a, b)
    t = 1
    while t > 0:
        t = c % d
        c, d = d, t
        print(t, c, d)
    answer = [c, int(a*b/c)]
    return answer

gcdlcm(31,25)

