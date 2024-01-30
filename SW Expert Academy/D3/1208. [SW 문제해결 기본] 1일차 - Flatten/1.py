import sys

sys.stdin = open("input.txt")

width = 100
for t in range(1, 11):
    dump = int(input())
    boxes = list(map(int, input().split()))
    heights = [0 for _ in range(101)]
    for box in boxes:
        heights[box] += 1
    bottom = 0
    top = 100
    while top >= bottom:
        if heights[bottom] == 0:
            bottom += 1
            continue
        if heights[top] == 0:
            top -= 1
            continue
        # print(bottom, top, heights[bottom], heights[top])
        if heights[bottom] < heights[top]: # heights[top]이 더 큰 경우
            dump -= heights[bottom]
            heights[bottom+1] += heights[bottom]
            heights[top] -= heights[bottom]
            heights[top-1] += heights[bottom]
            heights[bottom] = 0
        else: # heights[bottom]이 더 큰 경우
            dump -= heights[top]
            heights[top-1] += heights[top]
            heights[bottom] -= heights[top]
            heights[bottom+1] += heights[top]
            heights[top] = 0
        if dump <= 0:
            if dump == 0:
                if heights[bottom] == 0:
                    bottom += 1
                if heights[top] == 0:
                    top -= 1
            break
    print(f"#{t} {top - bottom}")
