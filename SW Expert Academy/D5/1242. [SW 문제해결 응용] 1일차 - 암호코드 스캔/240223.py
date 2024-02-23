import sys

sys.stdin = open('input.txt')


num_pic = {
    0: (3, 2, 1, 1), 
    1: (2, 2, 2, 1), 
    2: (2, 1, 2, 2), 
    3: (1, 4, 1, 1), 
    4: (1, 1, 3, 2), 
    5: (1, 2, 3, 1), 
    6: (1, 1, 1, 4), 
    7: (1, 3, 1, 2), 
    8: (1, 2, 1, 3), 
    9: (3, 1, 1, 2)
}


def CreateDic(n):
    new_dic = {}
    for i in num_pic:
        temp = ''
        for index, j in enumerate(num_pic[i]):
            if index % 2 == 0:
                temp += '0' * j * n
            else:
                temp += '1' * j * n
        new_dic[temp] = i
    return new_dic


def FindLength(raw_code):
    n = 1
    count = 1
    testcode = ''
    while True:
        for _ in range(7):
            testcode = raw_code[-count] + testcode
            count += 1
        if testcode in CreateDic(n):
            return n
        n += 1


def Decode(code, n):
    if code in checklist:
        return 0
    checklist[code] = 1
    check = 0
    result = 0
    dic = CreateDic(n)
    for i in range(8):
        one_code = ''
        for j in range(7*n*i, 7*n*(i+1)):
            one_code += code[j]
        num = dic[one_code]
        if i % 2 == 0:
            check += num * 3
        else:
            check += num
        result += num
    if check % 10:
        return 0
    return result


T = int(input())
for t in range(1, T+1):
    N, M = map(int, input().split())
    result = 0
    checklist = {}
    for _ in range(N):
        temp = bin(int(input().strip(), base=16)).strip('0')[1:]
        while temp:
            n = FindLength(temp)
            temp = temp.zfill(56 * n)
            result += Decode(temp[-56 * n:], n)
            temp = temp[:-56 * n].strip('0')
    print(f"#{t} {result}")

