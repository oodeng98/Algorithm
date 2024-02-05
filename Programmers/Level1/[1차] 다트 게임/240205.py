def solution(dartResult):
    score = [0]
    count = 0
    while count < len(dartResult) - 1:
        if dartResult[count].isdecimal():
            if dartResult[count+1] == '0':
                score.append(int(dartResult[count:count+2]))
                count += 1
            else:
                score.append(int(dartResult[count]))
            if dartResult[count+1] == 'S':
                pass
            elif dartResult[count+1] == 'D':
                score[-1] **= 2
            elif dartResult[count+1] == 'T':
                score[-1] **= 3
            if len(dartResult) - 1 < count + 2:
                break
            if dartResult[count+2] in ['*', '#']:
                if dartResult[count+2] == '*':
                    score[-1] *= 2
                    score[-2] *= 2
                else:
                    score[-1] *= -1
        count += 1
    print(score[1:])
    answer = sum(score)
    return answer