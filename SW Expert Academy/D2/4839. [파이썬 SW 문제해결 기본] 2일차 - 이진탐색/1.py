import sys


sys.stdin = open("input.txt")
T = int(input())
for t in range(1, T+1):
    P, Pa, Pb = map(int, input().split())
    al = 1
    ar = P
    bl = 1
    br = P
    acheck = 0
    bcheck = 0
    while True:
        if int((al + ar)/2) < Pa:
            al = int((al + ar)/2)
        elif Pa < int((al + ar)/2):
            ar = int((al + ar)/2)
        else:
            acheck = 1
        if int((bl + br)/2) < Pb:
            bl = int((bl + br)/2)
        elif Pb < int((bl + br)/2):
            br = int((bl + br)/2)
        else:
            bcheck = 1
        if acheck or bcheck:
            break
    if acheck:
        if bcheck:
            print(f"#{t} 0")
        else:
            print(f"#{t} A")
    else:
        print(f"#{t} B")
    