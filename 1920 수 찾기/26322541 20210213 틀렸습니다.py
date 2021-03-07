def search(lst1, lst2):
    lst1 = sorted(lst1)
    result = []
    for i in lst2:
        start = 0
        finish = len(lst1) - 1
        middle = (start + finish) // 2
        while True:
            if i < lst1[start] or lst1[finish] < i or start == middle:
                result.append(0)
                break
            if lst1[start] == i or lst1[middle] == i or lst1[finish] == i:
                result.append(1)
                break
            middle = (start + finish) // 2
            if lst1[middle] < i:
                start = middle
            else:
                finish = middle

    return result



num1 = int(input())
str1 = input().split()
for i in range(num1):
    str1[i] = int(str1[i])
num2 = int(input())
str2 = input().split()
for i in range(num2):
    str2[i] = int(str2[i])
result = search(str1, str2)

for i in result:
    print(i)