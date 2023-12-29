n = int(input())
# 각 줄에서 별의 수는 층*2-1
# 3, 6, 12, 24...
star = ['*', '* *', '*****']
count = [3]
while count[-1] < n:
    count.append(count[-1] * 2)
while len(star) < n:
    new_line = []
    j = 0
    for i in star:
        new_line.append(i + ' ' * ((len(star) + j) * 2 + 1 - len(i) * 2) + i)
        j += 1
    star.extend(new_line)
for i in star:
    front = (len(star) * 2 - len(i)) // 2
    print(' ' * front, end='')
    print(i, end='')
    print(' ' * front)


