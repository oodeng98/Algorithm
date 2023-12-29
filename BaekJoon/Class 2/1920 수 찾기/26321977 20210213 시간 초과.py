num1 = int(input())
str1 = input().split()
for i in range(num1):
    str1[i] = int(str1[i])
num2 = int(input())
str2 = input().split()
for i in range(num2):
    str2[i] = int(str2[i])

result = []
for i in str2:
    if i in str1:
        result.append(1)
    else:
        result.append(0)

for i in result:
    print(i)