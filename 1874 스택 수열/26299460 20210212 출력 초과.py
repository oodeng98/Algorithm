def push(stack, ele):  # 리스트의 마지막이 맨 위라고 생각
    stack.append(ele)


def pops(stack):
    check = stack[-1]
    stack.pop(len(stack) - 1)
    return check


num = int(input())
lst = [x for x in range(1, num + 1)]
sequence = []
for i in range(num):
    sequence.append(int(input()))
result = []
stack = []
remove_list = []
for i in range(sequence[0]):  # 처음엔 무조건 push해줘야함
    push(stack, i + 1)
    result.append('+')
    remove_list.append(i + 1)

for i in remove_list:
    lst.remove(i)


max_index = sequence.index(max(sequence))
i = 0
while i in range(max_index+1):  # sequence 넣고
    # stack의 맨 위 값과 sequence의 맨 앞 값을 비교해서 stack의 값이 더 크면 실패, stack의 값과 같으면 pop, stack의 값이 더 작으면 push
    # print(stack)
    if len(stack) == 0:
        push(stack, lst[0])
        lst.pop(0)
        result.append('+')
    value = stack[-1]
    # print(f'value:{value} sequence[i]:{sequence[i]} i:{i}')
    if value > sequence[i]:
        print('NO')
        break
    elif value == sequence[i]:
        result.append('-')
        pops(stack)
    else:
        while stack[-1] < sequence[i]:
            push(stack, lst[0])
            lst.pop(0)
            result.append('+')
        i -= 1
    i += 1

real = 0
for i in range(len(sequence[max_index:])-1):  # 이부분을 확인해주고, print를 그때그때 하지말고 저장해놓고 한번에 출력해야ㅐ함
    if sequence[i+max_index] < sequence[i+1+max_index]:
        real = 1
        print('NO')
    else:
        result.append('-')
if real == 0:
    for i in result:
        print(i)
"""
??-> 4까지 다넣고
4 -> 4를 빼고
3 -> 3을 빼고 6까지 넣음
6 ->6을 빼고 8까지 넣음
8 ->이제부터 다 뺌
7
5
2
1
"""
