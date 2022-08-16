def find_sequence(order, seq):
    max_index = seq.index(max(seq))
    result = 1
    while True:
        max_value = max(seq)
        max_index = seq.index(max_value)
        seq = seq[max_index:] + seq[:max_index]
        if order < max_index:
            order += len(seq) - max_index - 1
        elif order > max_index:
            order -= max_index + 1
        else:
            break
        seq.pop(0)
        result += 1
        if order > len(seq):
            order -= len(seq)
    return result


num = int(input())
data = []
for i in range(num*2):
    data.append(input().split())

for i in range(len(data)):
    for j in range(len(data[i])):
        data[i][j] = int(data[i][j])

target = [x[1] for x in data[0::2]]
sequence = data[1::2]

# print(target)
# print(sequence)

real_result = []
for i in range(num):
    real_result.append(find_sequence(target[i], sequence[i]))

for i in real_result:
    print(i)