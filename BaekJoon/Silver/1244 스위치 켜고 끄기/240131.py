import sys

input = sys.stdin.readline

length = int(input())
switch = [0] +  list(map(int, input().split()))
dic = {0: 1, 1: 0}
N = int(input())
for _ in range(N):
    s, num = map(int, input().split())
    if s == 1: # 남학생
        for i in range(num, length+1, num):
            switch[i] = dic[switch[i]]
    else: # 여학생
        switch[num] = dic[switch[num]]
        count = 1
        while True:
            if 1 <= num - count and num + count <= length:
                if switch[num-count] == switch[num+count]:
                    switch[num-count] = dic[switch[num-count]]
                    switch[num+count] = dic[switch[num+count]]
                    count += 1
                else:
                    break
            else:
                break
count = 0
for i in range(1, length+1):
    print(switch[i], end=' ')
    count += 1
    if count == 20:
        print()
        count = 0