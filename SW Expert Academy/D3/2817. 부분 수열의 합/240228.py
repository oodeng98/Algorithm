import sys

sys.stdin = open('input.txt')


def perm(n, index, total):
    if n == N or K <= total:
        if K == total:
            temp_dic = {}
            for i in lst:
                if i not in temp_dic:
                    temp_dic[i] = 1
                else:
                    temp_dic[i] += 1
            temp = 1
            for i in temp_dic:
                up = 1
                down = 1
                for j in range(temp_dic[i]):
                    up *= origin_dic[i] - j
                    down *= temp_dic[i] - j
                temp *= (up // down)
            result[0] += temp
    else:
        for i in range(index, length):
            if dic[nums[i]]:
                dic[nums[i]] -= 1
                lst.append(nums[i])
                perm(n+1, i, total+nums[i])
                dic[nums[i]] += 1
                lst.pop()


T = int(input())
for t in range(1, T+1):
    N, K = map(int, input().split())
    result = [0]
    dic = {}
    for i in map(int, input().split()):
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    origin_dic = dic.copy()
    nums = sorted(list(dic.keys()))
    length = len(nums)
    lst = []
    perm(0, 0, 0)
    print(f"#{t} {result[0]}")