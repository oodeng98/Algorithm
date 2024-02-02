def solution(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(participant)):
        if participant[i] != completion[i]:
            answer = participant[i]
            break
    return answer