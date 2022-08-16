num1 = int(input())
str1 = input().split()
num2 = int(input())
str2 = input().split()

result = []
for i in str2:
    if i in str1:
        result.append(1)
    else:
        result.append(0)

for i in result:
    print(i)