import sys

input = sys.stdin.readline
t = int(input())
for k in range(t):
    var = int(input())
    line_up = [0]
    line_down = [0]
    line_up.extend(list(map(int, input().split())))
    line_down.extend(list(map(int, input().split())))
    score_list = [[[0, "up"], [0, "down"]], [[line_up[1], "up"], [line_down[1], "down"]]]
    index = 2
    while index <= var:
        temp = []
        # up 을 향해 달려가는거임
        temp1 = score_list[index - 1][1][0] + line_up[index]  # down->up
        temp2 = score_list[index - 2][1][0] + line_up[index]  # down->black->up
        temp.append([max(temp1, temp2), "up"])
        score_list.append(temp)
        # down 을 향해 달려가는거임
        temp3 = score_list[index - 1][0][0] + line_down[index]  # up->down
        temp4 = score_list[index - 2][0][0] + line_down[index]  # up->blank->down
        temp.append([max(temp3, temp4), "down"])
        index += 1
    print(max(score_list[-1], key=lambda x: x[0])[0])
