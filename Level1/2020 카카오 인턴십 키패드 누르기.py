def solution(numbers, hand):
    answer= ''
    key_pad = [[1,2,3],[4,5,6],[7,8,9],['*', 0, '#']]
    # [1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5]
    L_now_row = 3
    L_now_col = 0
    R_now_row = 3
    R_now_col = 2
    for number in numbers:
        for row in key_pad:
            if number in row:
                if row.index(number) == 0:
                    answer+='L'
                    L_now_row = key_pad.index(row)
                    L_now_col = row.index(number)
                elif row.index(number) == 2:
                    answer+='R'
                    R_now_row = key_pad.index(row)
                    R_now_col = row.index(number)
                elif row.index(number) == 1:
                    L = abs(key_pad.index(row)-L_now_row)+abs(row.index(number)-L_now_col)
                    R = abs(key_pad.index(row)-R_now_row)+abs(row.index(number)-R_now_col)
                    if L<R:
                        answer +='L'
                        L_now_row = key_pad.index(row)
                        L_now_col = row.index(number)
                    elif L>R:
                        answer +='R'
                        R_now_row = key_pad.index(row)
                        R_now_col = row.index(number)
                    else:
                        answer += hand[0].upper()
                        if hand == 'right':
                            R_now_row = key_pad.index(row)
                            R_now_col = row.index(number)
                        else:
                            L_now_row = key_pad.index(row)
                            L_now_col = row.index(number)
                break
            else:
                pass

    return answer

numbers = [7, 0, 8, 2, 8, 3, 1, 5, 7, 6, 2]
hand = "left"

a = solution(numbers, hand)
print(a)

