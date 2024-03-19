import sys
from collections import deque


def X(ch1):
    if ch1 == "X":
        ch1 += "Q"
    else:
        ch1 += "X"
    return ch1


alpha = deque('A B C D E F G H I K L M N O P Q R S T U V W X Y Z'.split())
message = input().strip()
Key = deque(input().strip())

# step1
dic = {i: 0 for i in alpha}
table = [[] for _ in range(5)]
table_dic = {}
for i in range(5):
    for j in range(5):
        while Key and Key[0] not in dic:
            Key.popleft()
        if Key:
            del dic[Key[0]]
            c = Key.popleft()
        else:
            while alpha[0] not in dic:
                alpha.popleft()
            c = alpha.popleft()
        table[i].append(c)
        table_dic[c] = (i, j)

# step2
new_message = []
len_message = len(message)
index = 0
while index < len_message:
    temp_message = message[index]
    index += 1
    if index == len_message:
        temp_message += "X"
        new_message.append(temp_message)
        break
    if temp_message ==  message[index]:
        temp_message = X(temp_message)
    else:
        temp_message += message[index]
        index += 1
    new_message.append(temp_message)

# step3
result = ''
for i in new_message:
    x1, y1 = table_dic[i[0]]
    x2, y2 = table_dic[i[1]]
    if x1 == x2:
        result += table[x1][y1-4]
        result += table[x2][y2-4]
    elif y1 == y2:
        result += table[x1-4][y1]
        result += table[x2-4][y2]
    else:
        result += table[x1][y2]
        result += table[x2][y1]
print(result)