import sys


input = sys.stdin.readline
n = int(input())

dic = {0: 0}
count = 0
while True:
    count += 1
    for i in list(dic.keys()):
        if i * 2 not in dic:
            dic[i * 2] = i
        if i - 1 > 0 and i - 1 not in dic:
            dic[i - 1] = i
        if i + 1 not in dic:
            dic[i + 1] = i
    if n in dic:
        break
order = []
target = n
while target in dic and target != 0:
    order.append(target)
    target = dic[target]
order.reverse()
cal_order = []
for i in range(len(order) - 1):
    if order[i + 1] % order[i] == 0:
        cal_order.append('*2')
    elif order[i + 1] - order[i] == 1:
        cal_order.append('+1')
    else:
        cal_order.append('-1')
del order[0]
# print(cal_order)
# print(order)
fibo = {0: 0, 1: 1, 2: 1}
for i in range(len(cal_order)):
    # print(cal_order[i], '=', order[i])
    target = order[i]
    if cal_order[i] == '*2':
        k = target // 2
        fibo[order[i] - 1] = (fibo[k - 1] ** 2 + fibo[k] ** 2) % 1000000007
        fibo[order[i]] = (fibo[k] ** 2 + 2 * fibo[k] * fibo[k - 1]) % 1000000007
    elif cal_order[i] == '+1':
        fibo[order[i]] = fibo[order[i] - 1] + fibo[order[i] - 2] % 1000000007
    else:
        fibo[order[i] - 1] = fibo[order[i] + 1] - fibo[order[i]] % 1000000007
        # fibo[order[i]] = fibo[order[i] + 2] - fibo[order[i] + 1] % 1000000007

print(fibo[n])