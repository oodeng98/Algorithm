def solution(n):
    arr = [i for i in range(n + 1)]
    for i in range(2, n+1):
        if arr[i]:
            count = 2
            while i * count <= n:
                arr[i * count] = 0
                count += 1
    answer = len(set(arr)) - 2
    return answer