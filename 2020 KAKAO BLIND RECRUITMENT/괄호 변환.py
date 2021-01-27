def good(p,v):
    # 올바른 문자열 인지 아닌지 확인
    answer = ''
    fro = p[:len(p)//2] #'(()('
    a = p[len(p)//2:] #'))()'
    back = []
    if v == '':
        if ''.join(p)=='()':
            return '()'
    while a:
        f = fro.pop(0)
        A = a.pop()
        if f==')':# 올바른 문자열 아님
            answer ='('
            break
    if answer == '(':
        answer += solution(v)
        answer +=')'
        p = p[1:-1]
        for i in p:
            if i==')':
                answer+='('
            else:
                answer+=')'
    else:
        if ''.join(p)==')(':
            answer = ['(',')']
        else:
            answer = p
        answer+=solution(v)
    return answer
def solution(p):
    # 빈문자열 확인 --> 빈문자 == 빈문자 return
    p = list(p)
    if len(p) == 0:
        return ''
    if len(p) == 2:
        Answer = good(p,'')
        return ''.join(Answer)
    # u, v 분리
    left, right = 0, 0
    for i in range(len(p)):
        if p[i] == '(':
            right +=1
        else:
            left +=1
        if left == right:
            u = p[:i+1]
            v = p[i+1:]
            break
    answer = good(u,v)

    # 분리
    # 문자열 p 분리 균형문자열 u, 나머지 v
    # u가 올바른 문자열이면
    # v를 처음부터 실행  --> 재귀
    return ''.join(answer)
p = "(()())()"
a = solution(p)
print(a)