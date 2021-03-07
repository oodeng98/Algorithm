data = []
while True:
    d = str(int(input()))
    if d == '0':
        break
    data.append(d)

print(data)

for i in data:
    check = 0
    if len(i) == 1:
        print('yes')
        continue
    for j in range(len(i) // 2):
        if i[j] != i[-(j+1)]:
            print('no')
            check = 1
            break
    if check == 0:
        print('yes')