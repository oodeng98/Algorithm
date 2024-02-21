import sys

sys.stdin = open('input.txt')


def heappush(n):
    heap.append(n)
    hlength = length
    while hlength and heap[hlength] < heap[hlength // 2]:
        heap[hlength], heap[hlength // 2] = heap[hlength // 2], heap[hlength]
        hlength //= 2

T = int(input())
for t in range(1, T+1):
    N = int(input())
    heap = [0]
    length = 0
    for i in map(int, input().split()):
        length += 1
        heappush(i)

    total = 0
    while length // 2:
        total += heap[length // 2]
        length //= 2
    print(f"#{t} {total}")
