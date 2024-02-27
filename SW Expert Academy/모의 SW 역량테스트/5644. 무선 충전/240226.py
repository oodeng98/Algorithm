import sys

sys.stdin = open('input.txt')


def Move(direction):
    if direction == 0:
        return 0, 0
    elif direction == 1:
        return 0, -1
    elif direction == 2:
        return 1, 0
    elif direction == 3:
        return 0, 1
    elif direction == 4:
        return -1, 0
    

def Area(x, y, c):
    for i in range(-c, c+1):
        for j in range(-c+abs(i), c-abs(i)+1):
            if 1 <= x + i <= 10 and 1 <= y + j <= 10:
                yield x + i, y + j


T = int(input())
for t in range(1, T+1):
    M, A = map(int, input().split())
    A_move = list(map(int, input().split()))
    B_move = list(map(int, input().split()))
    BC_list = [list(map(int, input().split())) for _ in range(A)]
    BC_list.sort(key=lambda x: x[-1], reverse=True)
    charge = {}
    for index, i in enumerate(BC_list):
        x, y, c, p = i
        for a, b in Area(x, y, c):
            if (a, b) in charge:
                charge[(a, b)].append((p, index))
            else:
                charge[(a, b)] = [(p, index)]
    
    a1, a2 = 1, 1
    b1, b2 = 10, 10
    result = 0
    if (a1, a2) in charge:
        result += charge[(a1, a2)][0][0]
    if (b1, b2) in charge:
        result += charge[(b1, b2)][0][0]
    for m in range(M):
        da1, da2 = Move(A_move[m])
        a1, a2 = a1 + da1, a2 + da2
        db1, db2 = Move(B_move[m])
        b1, b2 = b1 + db1, b2 + db2
        if (a1, a2) in charge:
            result += charge[(a1, a2)][0][0]
            if (b1, b2) in charge:
                charge_a = charge[(a1, a2)][0]
                charge_b = charge[(b1, b2)][0]
                if charge_a[1] == charge_b[1]:
                    temp_a, temp_b = 0, 0
                    if 1 < len(charge[(a1, a2)]):
                        temp_a = charge[(a1, a2)][1][0]
                    if 1 < len(charge[(b1, b2)]):
                        temp_b = charge[(b1, b2)][1][0]
                    result += max(temp_a, temp_b)
                else:
                    result += charge[(b1, b2)][0][0]
        else:
            if (b1, b2) in charge:
                result += charge[(b1, b2)][0][0]
    print(f"#{t} {result}")