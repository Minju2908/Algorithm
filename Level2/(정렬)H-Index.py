def solution(citations):
    answer = 0
    for i in range(1,len(citations)+1):
        paper = [index for index in citations if index>=i]
        if len(paper)>answer and len(citations)-len(paper)<=i:
            answer = i

    return answer