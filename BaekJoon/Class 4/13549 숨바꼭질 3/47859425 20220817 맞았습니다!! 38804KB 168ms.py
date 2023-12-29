import sys
import heapq

input = sys.stdin.readline
n, k = map(int, input().split())

if n > k:
    print(n - k)
else:
    check = {n: 0}
    heap = []
    heapq.heappush(heap, (0, n))
    while True:
        tup = heapq.heappop(heap)
        if tup[1] == k:
            print(tup[0])
            break
        else:
            if 2 * tup[1] <= 100000 and 2 * tup[1] not in check:
                check[2 * tup[1]] = 0
                heapq.heappush(heap, (tup[0], 2 * tup[1]))
            if tup[1] + 1 <= 100000 and tup[1] + 1 not in check:
                check[tup[1] + 1] = 0
                heapq.heappush(heap, (tup[0] + 1, tup[1] + 1))
            if 0 <= tup[1] - 1 and tup[1] - 1 not in check:
                check[tup[1] - 1] = 0
                heapq.heappush(heap, (tup[0] + 1, tup[1] - 1))
