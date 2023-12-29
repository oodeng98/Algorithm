import sys

input = sys.stdin.readline
sys.setrecursionlimit(20000)

# 입력 파트
P = []
while True:
    node = input().strip()
    if not node:
        break

    P.append(int(node))


def postorder(start, end):
    if start + 1 >= end:  # 길이가 1인 경우
        print(P[start])
        return

    if P[start] < P[start + 1] or P[start] > P[end - 1]:  # 루트 노드 구분 방법
        postorder(start + 1, end)
    else:
        r = end
        for i in range(start + 1, end):
            if P[start] < P[i]:
                r = i
                break

        postorder(start + 1, r)
        postorder(r, end)
    print(P[start])


postorder(0, len(P))
'''
내가 생각하지 못한 루트 노드 구분 방법이 존재했고, 리스트 형태로 recursion을 돌리지 말고 시작, 끝 index를 넘겨주는 것이 훨씬 효율적이다.
'''
