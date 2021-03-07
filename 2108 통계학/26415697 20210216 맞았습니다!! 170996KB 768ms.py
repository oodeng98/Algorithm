num = int(input())
data = []
for i in range(num):
    data.append(int(input()))

san = 0
count = {}
for i in data:
    if i in count.keys():
        count[i] += 1
    else:
        count[i] = 1
    san += i
san = san / num
if int(san) * 2 == int(san * 2):
    print(int(san))
else:
    if san < 0:
        print(int(san-1))
    else:
        print(int(san+1))

data_sorted = sorted(data)
print(data_sorted[num//2])

count = [(x, y) for x, y in count.items()]
count = sorted(count, key=lambda x: x[0])
count = sorted(count, key=lambda x: x[1], reverse=True)
if len(count) > 1:
    if count[0][1] == count[1][1]:
        print(count[1][0])
    else:
        print(count[0][0])
else:
    print(count[0][0])

print(data_sorted[-1] - data_sorted[0])