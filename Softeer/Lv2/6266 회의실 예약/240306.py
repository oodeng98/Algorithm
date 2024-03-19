import sys

N, M = map(int, input().split())
meeting_room = [input() for _ in range(N)]
meeting_room.sort()
schedule = {}
for m in meeting_room:
    schedule[m] = [(9, 9), (18, 18)]
for _ in range(M):
    r, s, t = input().split()
    schedule[r].append((int(s), int(t)))    

for i in meeting_room:
    schedule[i].sort()
    print(f"Room {i}:")
    count = 0
    result = ''
    for j in range(len(schedule[i])-1):
        a, b = schedule[i][j][1], schedule[i][j+1][0]
        if a < b:
            count += 1
            if a == 9:
                result += f"0{a}-{b}\n"
                continue
            result += f"{a}-{b}\n"
    if not count:
        print("Not available")
    else:
        print(f"{count} available:")
        print(result, end='')
    if i == meeting_room[-1]:
        break
    print('-----')