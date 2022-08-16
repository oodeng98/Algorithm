def push(stack, lst):
    stack.append(lst[0])
    lst.pop(0)


def pull(stack):
    return stack


num = int(input())
sequence = []
result = []
stack = []

for i in range(num):
    sequence.append(int(input()))
input_list = [x for x in range(sequence[0], num+2)]

for i in range(sequence[0]):
    result.append('+')

for i in range(num):
    if i == num-1:
        result.append('-')
        break
    data = pull(stack)
    result.append('-')
    if sequence[i] < sequence[i+1]:
        while input_list[0] < sequence[i+1]:
            push(stack, input_list)
            result.append('+')
        if input_list[0] != sequence[i+1]:
            result = ['NO']
            break
    else: # sequence[i] > sequence[i+1]
        while data == sequence[i+1]:
            data = pull(stack)
            result.append('-')
for i in result:
    print(i)