import sys

input = sys.stdin.readline
t = int(input())
for k in range(t):
    var = int(input())
    line1 = list(map(int, input().split()))
    line2 = list(map(int, input().split()))
    line1.append(0)
    line2.append(0)
    results = []
    for i in range(2):
        if i == 0:
            result = line1[0]
            n = [0, "down"]
        else:
            result = line2[0]
            n = [0, "up"]
        while True:
            if n[0] >= var - 1:
                break
            if n[1] == "down":
                if line2[n[0] + 1] + line1[n[0] + 2] < line2[n[0] + 2]:
                    result += line2[n[0] + 2]
                    n[0] += 2
                else:
                    result += line2[n[0] + 1]
                    n[0] += 1
                n[1] = "up"
            else:
                if line1[n[0] + 1] + line2[n[0] + 2] < line1[n[0] + 2]:
                    result += line1[n[0] + 2]
                    n[0] += 2
                else:
                    result += line1[n[0] + 1]
                    n[0] += 1
                n[1] = "down"
        results.append(result)
    print(max(results))