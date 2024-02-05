def solution(n, arr1, arr2):
    answer = []
    for i in range(n):
        temp = ''
        for j in range(n):
            if arr1[i] & (1<<j) or arr2[i] & (1<<j):
                temp = '#' + temp
            else:
                temp = ' ' + temp
        answer.append(temp)
    return answer