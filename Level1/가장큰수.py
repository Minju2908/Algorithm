

# def solution(numbers):
#     arr = []
#     sol = []
#     answer = ''
#     for i in numbers:
#         val = i%10
#         arr.append(val)
#     while(1):
#         if len(arr)>0:
#             max_val = max(arr)
#             pos = arr.index(max_val)
#             sol.append(numbers[pos])
#             del arr[pos]
#             del numbers[pos]
#         else:
#             break
#     for i in sol:
#         answer += str(i)
#     print(answer)
#
# numbers = [3,30,304,5,9]
# solution(numbers)

a = [1,9,2,8,9]
b=max(a)
count=0
for i in a:
    if (i == b):
        count = count+1