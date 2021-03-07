import sys


input = sys.stdin.readline
n = int(input())
num = int(input())
data = input().rstrip()
data_transform = []
temp = ''
check = 0
for i in range(num - 2):
    if check != 1:
        if data[i] == 'I' and data[i+1] == 'O' and data[i+2] == 'I':
            temp += '1'
            check = 1
        else:
            data_transform.append(temp)
            temp = ''
    else:
        check -= 1
data_transform.append(temp)
result = 0
for i in data_transform:
    result += max(0, len(i) - n + 1)
print(result)