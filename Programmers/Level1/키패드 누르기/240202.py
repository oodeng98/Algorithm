def solution(numbers, hand):
    left = [0, 0]
    right = [2, 0]
    left_key = {1: 3, 4: 2, 7: 1}
    right_key = {3: 3, 6: 2, 9: 1}
    middle_key = {2: 3, 5: 2, 8: 1, 0: 0}
    answer = ''
    for i in numbers:
        if i in left_key:
            answer += 'L'
            left = [0, left_key[i]]
        elif i in right_key:
            answer += 'R'
            right = [2, right_key[i]]
        else:
            pos = [1, middle_key[i]]
            left_distance = abs(left[0] - pos[0]) + abs(left[1] - pos[1])
            right_distance = abs(right[0] - pos[0]) + abs(right[1] - pos[1])
            if right_distance < left_distance:
                right = pos
                answer += 'R'
            elif left_distance < right_distance:
                left = pos
                answer += 'L'
            else:
                if hand == 'left':
                    left = pos
                    answer += 'L'
                else:
                    right = pos
                    answer += 'R'
    return answer
'''
LRLLLRLLLRL
LRLLLRLLRRL
'''