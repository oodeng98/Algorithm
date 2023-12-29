num = int(input())
data = input()
# print(ord('a'))  # 97
result = 0
for i in range(len(data)):
    temp = 1
    for j in range(i):
        temp *= 31
    result += (ord(data[i]) - 96) * temp
print(result % 1234567891)