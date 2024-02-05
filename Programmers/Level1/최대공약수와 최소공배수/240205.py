def solution(n, m):
    answer = []
    a, b = min(n, m), max(n, m)
    for i in range(a+1, 0, -1):
        if a % i == 0 and b % i == 0:
            answer.append(i)
            break
    temp = b
    count = 2
    while True:
        if temp % a == 0:
            answer.append(temp)
            break
        temp = b * count
        count += 1
        
    return answer