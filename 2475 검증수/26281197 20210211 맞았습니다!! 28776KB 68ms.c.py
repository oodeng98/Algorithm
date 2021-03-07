# 0 4 2 5 6
data = input().split(' ')
total = 0
for i in data:
    total += int(i) * int(i)

print(total % 10)

