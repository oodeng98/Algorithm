import sys


def fibo(des):
    if des == 0:
        return 0
    if des == 1:
        return 1
    if des not in dic:
        k = (des + 1) // 2
        if k not in dic:
            temp1 = fibo(k)
            dic[k] = temp1
        else:
            temp1 = dic[k]
        if k - 1 not in dic:
            temp2 = fibo(k - 1)
            dic[k - 1] = temp2
        else:
            temp2 = dic[k - 1]
        if des % 2 == 0:
            dic[des] = (temp1 ** 2 + 2 * temp1 * temp2) % 1000000007
            return dic[des]
        else:
            dic[des] = (temp1 ** 2 + temp2 ** 2) % 1000000007
            return dic[des]


input = sys.stdin.readline
n = int(input())
dic = {0: 0, 1: 1, 2: 1}
fibo(n)
print(dic[n])