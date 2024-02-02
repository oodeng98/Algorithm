def solution(answers):
    N = len(answers)
    num1 = [1, 2, 3, 4, 5] * (N // 5 + 1)
    num2 = [2, 1, 2, 3, 2, 4, 2, 5] * (N // 8 + 1)
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * (N // 10 + 1)
    result = [0, 0, 0]
    for i, j, k, ans in zip(num1, num2, num3, answers):
        if i == ans:
            result[0] += 1
        if j == ans:
            result[1] += 1
        if k == ans:
            result[2] += 1
    answer = [i + 1 for i in range(3) if result[i] == max(result)]
    return answer