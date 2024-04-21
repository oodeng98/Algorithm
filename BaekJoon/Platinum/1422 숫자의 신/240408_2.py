import sys


input = sys.stdin.readline
k, n = map(int,input().split())
lst = [input().strip() for _ in range(k)]

# 길이가 길고 그중에서 숫자가 가장 큰 애가 앞으로 오게끔 정렬
lst.sort(key =lambda x:(-len(x),-int(x)))
num = lst + [lst[0]] * (n-k)
length = len(lst[0])
num.sort(key=lambda x: x*length, reverse=True)  # 최소 길이를 맞춰주고 비교
print(''.join(num))