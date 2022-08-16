import sys

input = sys.stdin.readline
t = int(input())
for k in range(t):
    var = int(input())
    line1 = [0]
    line2 = [0]
    line1.extend(list(map(int, input().split())))
    line2.extend(list(map(int, input().split())))
    score_list = [(0, "down"), (line1[1], "up")]  # 위쪽 하나를 먹고 시작한다고 가정
    index = 2
    while index <= var:
        if score_list[index - 2][1] == "down":
            candidate_1 = (score_list[index - 2][0] + line1[index], "up")
        else:
            candidate_1 = (score_list[index - 2][0] + line2[index], "down")
        if score_list[index - 1][1] == "down":
            candidate_2 = (score_list[index - 1][0] + line1[index], "up")
        else:
            candidate_2 = (score_list[index - 1][0] + line2[index], "down")
        score_list.append(max(candidate_1, candidate_2, key=lambda x: x[0]))
        index += 1
    temp_max = score_list[-1][0]

    score_list = [(0, "up"), (line2[1], "down")]  # 아래쪽 하나를 먹고 시작한다고 가정
    index = 2
    while index <= var:
        if score_list[index - 2][1] == "down":
            candidate_1 = (score_list[index - 2][0] + line1[index], "up")
        else:
            candidate_1 = (score_list[index - 2][0] + line2[index], "down")
        if score_list[index - 1][1] == "down":
            candidate_2 = (score_list[index - 1][0] + line1[index], "up")
        else:
            candidate_2 = (score_list[index - 1][0] + line2[index], "down")
        score_list.append(max(candidate_1, candidate_2, key=lambda x: x[0]))
        index += 1
    print(max(score_list[-1][0], temp_max))
