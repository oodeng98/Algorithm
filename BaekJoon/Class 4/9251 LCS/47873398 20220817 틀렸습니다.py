import sys

input = sys.stdin.readline
temp1 = input().strip()
temp2 = input().strip()

if len(temp1) < len(temp2):
    str1 = temp1
    str2 = temp2
else:
    str1 = temp2
    str2 = temp1

# 첫번째 문장의 알파벳들이 두번째 문장에서 각각 몇번째에 위치하는지 적어놓고
# 그 숫자들을 아래에서부터 가장 긴 수열로 만들어주면?
arr = []
for i in str1:
    temp = []
    for index, j in enumerate(str2):
        if i == j:
            temp.append((i, index))
    if not temp:
        continue
    arr.append(temp)

max_length = 0
for index in range(len(arr)):
    min_index = min(arr[index], key=lambda x: x[1])[1]
    result = ''
    for i in arr[index:]:
        for j in i:
            if j[1] >= min_index:
                min_index = j[1]
                result += j[0]
                break
    max_length = max(max_length, len(result))
print(max_length)