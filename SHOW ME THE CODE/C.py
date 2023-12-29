import sys


def show_scoreboard():
    for i in scoreboard:
        for j in i:
            print(j, end=' ')
        print()

input = sys.stdin.readline
N, M, C = map(int, input().split())
sat = [[0]]
for i in range(C):
    sat.append([0] + list(map(int, input().split())))
A_univ = list(map(int, input().split()))
B_univ = list(map(int, input().split()))

first_floor = [sat[A_univ[0]][B_univ[0]]]
for j in range(1, M):
    first_floor.append(max(first_floor[-1], sat[A_univ[0]][B_univ[j]]))
scoreboard = [first_floor]
for i in range(1, N):
    next_floor = [max(sat[A_univ[i]][B_univ[0]], scoreboard[i - 1][0])]
    for j in range(1, M):
        next_floor.append(max(next_floor[j - 1], scoreboard[i - 1][j],
                              scoreboard[i - 1][j - 1] + sat[A_univ[i]][B_univ[j]]))
    scoreboard.append(next_floor)
# show_scoreboard()
print(scoreboard[N - 1][M - 1])
'''
2 3 3
10 4 1
4 5 6
1 6 9
1 2 
1 2 3
'''
