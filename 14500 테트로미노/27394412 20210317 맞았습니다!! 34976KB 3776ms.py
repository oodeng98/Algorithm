import sys


def line(paper):
    result = 0
    for i in paper:  # 가로로 4개 연속인 경우
        for j in range(len(i) - 3):
            temp = i[j] + i[j + 1] + i[j + 2] + i[j + 3]
            result = max(result, temp)
    for i in range(len(paper) - 3):  # 세로로 4개 연속인 경우
        for j in range(len(paper[0])):
            temp = paper[i][j] + paper[i + 1][j] + paper[i + 2][j] + paper[i + 3][j]
            result = max(result, temp)
    return result


def take_six(paper):
    result = 0
    except_case = [(1, 5), (2, 4), (2, 5), (3, 5), (2, 6)]
    for i in range(len(paper) - 2):  # 세로로 세웠을 때
        for j in range(len(paper[0]) - 1):
            temp = [(1, paper[i][j]), (2, paper[i + 1][j]), (3, paper[i + 2][j]), (4, paper[i][j + 1]),
                    (5, paper[i + 1][j + 1]), (6, paper[i + 2][j + 1])]
            process = []
            for k in range(5):
                for l in range(1, 6 - k):
                    process.append(((temp[k][0], temp[k + l][0]), temp[k][1] + temp[k + l][1]))
            process.sort(key=lambda x: x[1])
            count = 0
            while True:
                if process[count][0] in except_case:
                    count += 1
                else:
                    break
            num_temp = 0
            for k in temp:
                num_temp += k[1]
            result = max(num_temp - process[count][1], result)
    for i in range(len(paper) - 1):  # 가로로 눕혔을 때
        for j in range(len(paper[0]) - 2):
            temp = [(1, paper[i + 1][j]), (2, paper[i + 1][j + 1]), (3, paper[i + 1][j + 2]), (4, paper[i][j]),
                    (5, paper[i][j + 1]), (6, paper[i][j + 2])]
            process = []
            for k in range(5):
                for l in range(1, 6 - k):
                    process.append(((temp[k][0], temp[k + l][0]), temp[k][1] + temp[k + l][1]))
            process.sort(key=lambda x: x[1])
            count = 0
            while True:
                if process[count][0] in except_case:
                    count += 1
                else:
                    break
            num_temp = 0
            for k in temp:
                num_temp += k[1]
            result = max(num_temp - process[count][1], result)
    return result


input = sys.stdin.readline
col, row = map(int, input().split())
data = []
for i in range(col):
    data.append(list(map(int, input().split())))
print(max(line(data), take_six(data)))