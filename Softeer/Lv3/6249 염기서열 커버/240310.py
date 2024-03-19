import sys

input = sys.stdin.readline

def check(seq1, seq2):
    result = ''
    for i in range(M):
        if seq1[i] == seq2[i]:
            result += seq1[i]
        else:
            if seq1[i] == '.':
                result += seq2[i]
            elif seq2[i] == '.':
                result += seq1[i]
            else:
                return False
    return result


def dfs(n):
    if n == N:
        global result
        p = len(parent)
        if p < result:
            result = p
        return
    if result <= len(parent):
        return
    for i in range(len(parent)):
        temp = check(parent[i], lst[n])
        if temp:
            temp_p = parent[i]
            parent[i] = temp  # 기존 초염기서열 갱신
            dfs(n+1)
            parent[i] = temp_p  # 되돌려주고

    parent.append(lst[n])  # 새로운 초염기서열 추가
    dfs(n+1)
    parent.pop()


N, M = map(int, input().split())
lst = [input() for _ in range(N)]
parent = [lst[0]]
result = N
dfs(1)
print(result)