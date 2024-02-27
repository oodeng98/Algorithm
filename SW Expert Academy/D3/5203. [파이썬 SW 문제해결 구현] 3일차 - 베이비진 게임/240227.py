import sys

sys.stdin = open('input.txt')


def Run(count, n):
    if 3 <= count[n]:
        return True
    return False


def Triplet(player, n):
    left = 0
    right = 0
    j = 1
    while 0 <= n - j and player[n-j] == 1:
        left += 1
        j += 1
    j = 1
    while n + j < 10 and player[n+j] == 1:
        right += 1
        j += 1
    if 2 <= left + right:
        return True
    return False


T = int(input())
for t in range(1, T+1):
    print(f"#{t}", end=' ')
    player1 = [0 for _ in range(10)]
    player1_count = {i: 0 for i in range(10)}
    player2 = [0 for _ in range(10)]
    player2_count = {i: 0 for i in range(10)}
    cards = map(int, input().split())
    check = 1
    for index, i in enumerate(cards):
        if index % 2:
            player2_count[i] += 1
            player2[i] = 1
            if Run(player2_count, i) or Triplet(player2, i):
                print(2)
                check = 0
                break
        else:
            player1_count[i] += 1
            player1[i] = 1
            if Run(player1_count, i) or Triplet(player1, i):
                print(1)
                check = 0
                break
    if check:
        print(0)
