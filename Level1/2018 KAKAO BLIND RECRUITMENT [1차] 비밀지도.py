def solution(n, arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        a = [format(i, 'b').zfill(n)]
        b = [format(j, 'b').zfill(n)]
        for x,y in zip(a,b):
            s = str(int(x) + int(y)).zfill(n)
            ans = ""
            for v in s:
                if v == '0':
                    ans+=' '
                elif v =='1' or v=='2':
                    ans+='#'
        answer.append(ans)
    return answer
