num = int(input())
data = []
for i in range(num):
    data.append(int(input()))

# 산술평균
san = 0
for i in data:
    san += i
san = san / num
if int(san) * 2 == int(san * 2):
    print(int(san))
else:
    print(int(san+1))

# 중앙값
data_sorted = sorted(data)
print(data_sorted[num//2])

# 최빈값, 두번째로 작은 값 출력해야함
count = {}
for i in data:
    if i in count.keys():
        count[i] += 1
    else:
        count[i] = 1

count = [(x, y) for x, y in zip(count.keys(), count.values())]
count = sorted(count, key=lambda x: x[1], reverse=True)
if count[0][1] == count[1][1]:
    count = sorted(count, key=lambda x: x[0])
    print(count[1][0])
else:
    print(count[0][0])

# 범위
print(data_sorted[-1] - data_sorted[0])

# print(round(-2.6))
