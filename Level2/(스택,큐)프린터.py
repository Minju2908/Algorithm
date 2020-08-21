
def solution(print_list, location):
    val = print_list[location]
    answer = 0
    while print_list:
        if val != max(print_list):
            for i in print_list:
                if i < max(print_list):
                    print_list.append(i)
                    print_list.pop(0)
                    if location == 0:
                        location = len(print_list)-1
                    else:
                        location -= 1
                    break
                elif i == max(print_list):
                    print_list.pop(0)
                    answer += 1
                    if location == 0:
                        location = len(print_list) - 1
                    else:
                        location -= 1
                    break
        else:
            count = 0
            for i in print_list[:location]:
                if i == val:
                    count+=1
            return answer+count+1

def solution2(priorities, location):
    queue = [(i,p) for i,p in enumerate(priorities)]
    answer = 0
    while True:
        cur = queue.pop(0)
        if any(cur[1] < q[1] for q in queue):
            queue.append(cur)               # cur[1] 보다 큰 수 가 있으니까 뒤로 뺌
        else:  # 큰 수가 하나도 없으면
            answer += 1                     # 1증가하고
            if cur[0] == location:          #
                return answer

priorities = [1,1,9,1,1,1]
location = 0
a = solution2(priorities, location)
print(a)