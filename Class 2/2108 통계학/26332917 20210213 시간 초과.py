num = int(input())
data = []
for i in range(num):
    data.append(int(input()))

# 산술평균
san = 0
for i in data:
    san += i
san = san / num
check = 0
if san < 0:
    san = san * (-1)
    check = 1
san_check = san * 10
if san_check % 10 >= 5:
    san = int(san) + 1
else:
    san = int(san)

if check == 0:
    print(san)
else:
    print(-san)

# 중앙값
data_sorted = sorted(data)
print(data_sorted[num//2])

# 최빈값
cho_check = list(set(data))
fre = 0
fre_ele = 0
for i in cho_check:
    if data.count(i) > fre:
        fre = data.count(i)
        fre_ele = i
print(fre_ele)

# 범위
print(data_sorted[-1] - data_sorted[0])
