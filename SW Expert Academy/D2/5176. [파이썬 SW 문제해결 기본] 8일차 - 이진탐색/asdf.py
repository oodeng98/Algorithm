def tree(n):
    global num
    if n <= N:
        # 좌측 노드
        tree(n * 2)
        # n이 N보다 커지면 n위치에 num(순서) 저장
        arr[n] = num
        # 저장 후, 다음 순서
        num += 1
        # 우측 노드 찾기
        tree(n * 2 + 1)

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [0 for i in range(N + 1)]
    num = 1
    tree(1)
    # 루트 : 시작 노드
    print(f'#{tc} {arr[1]} {arr[N // 2]}')