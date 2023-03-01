def mul(mat1, mat2):
    ret = [[] for _ in range(n)]
    for i in range(n):
        for j in range(n):
            temp = 0
            for k in range(n):
                temp += mat1[i][k] * mat2[k][j]
            ret[i].append(temp % 1000)
    return ret


n, b = map(int, input().split())
matrix = []
result = []
for i in range(n):
    matrix.append(list(map(int, input().split())))
    temp = [0 for _ in range(n)]
    temp[i] = 1
    result.append(temp)

a = str(bin(b))[2:][::-1]
index = len(a) - 1

via = matrix
for i in a:
    if i == '1':
        result = mul(result, via)
    via = mul(via, via)

for i in result:
    for j in i:
        print(j, end=' ')
    print()
