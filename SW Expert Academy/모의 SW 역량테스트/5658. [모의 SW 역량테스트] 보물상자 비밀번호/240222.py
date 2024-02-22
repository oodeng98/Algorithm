import sys

sys.stdin = open('input.txt')


T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    num = input().rstrip()
    nums = set()
    length = N // 4
    for i in range(length):
        for j in range(4):
            temp = ''
            for k in range(length*j+i, length*(j+1)+i):
                temp += num[k % N]
            nums.add(int(temp, 16))
    print(f"#{t} {sorted(list(nums), reverse=True)[K-1]}")
