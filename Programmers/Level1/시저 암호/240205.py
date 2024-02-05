def solution(s, n):
    answer= ''
    Alpha = {i: chr(65 + i) for i in range(26)}
    alpha = {i: chr(97 + i) for i in range(26)}
    for c in s:
        if c == ' ':
            answer += c
        elif c.isupper():
            answer += Alpha[(ord(c) - 65 + n) % 26]
        elif c.islower():
            answer += alpha[(ord(c) - 97 + n) % 26]
    return answer
