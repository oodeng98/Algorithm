def solution(new_id):
    # 1
    answer = new_id.lower()
    # 2
    temp = ''
    for c in answer:
        if c.isdigit() or c.isalpha() or c == '-' or c == '_' or c == '.':
            temp += c
    # 3
    answer = ''
    index = 0
    while True:
        if temp[index] == '.':
            answer += temp[index]
            while temp[index] == '.':
                index += 1
                if index >= len(temp):
                    break
        else:
            answer += temp[index]
            index += 1
        if index >= len(temp):
            break
    # 4
    answer = answer.strip('.')
    # 5
    if not answer:
        answer = 'a'
    # 6
    if len(answer) >= 16:
        answer = answer[:15]
        while answer[-1] == '.':
            answer = answer[:len(answer)-1]
    # 7
    while len(answer) < 3:
        answer += answer[-1]
    return answer