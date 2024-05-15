import sys
from collections import deque
from heapq import heappush, heappop

input = sys.stdin.readline
N, K, M = map(int, input().split())
cows_check = [0 for _ in range(N)]
price = deque([])
regular = []
discount = []
for i in range(N):
    r, d = map(int, input().split())
    regular.append((r, i))
    discount.append((d, i))
    price.append((r, d, i, 'regular'))
    price.append((d, r, i, 'discount'))
regular.sort()
discount.sort()
price.sort()

discount_cows = []
while 0 <= M:
    price, other_price, index, price_type = price.popleft()
    if price_type == 'discount':
        if len(discount_cows) < K:
            discount_cows.heappush((price, index))
        else:
            pass
    break

'''
쿠폰가와 정가 기준으로 싼 소를 구입하면서 진행
쿠폰가로 산 소가 K마리가 넘는 경우는 어떻게 할 것인가?
쿠폰가로 산 소의 정가가 내가 사야하는 소의 정가보다 싸다면?
그렇다면 소를 정가로 구입하고 쿠폰은 다음 소에게 넘겨준다?
쿠폰은 사실 아낄 수 있는 돈을 의미하지 소의 절대적 가격을 보면 안댐
쿠폰가 기준 다음으로 싼 소가 아낄 수 있는 돈이 더 큰가?
정가 - 쿠폰가 = 차액 이라고 하면
쿠폰으로 산 소들 중 차액이 가장 작은 애를 정가로 빼주면 되는 것이 아닌가?
8, 3이라고 치면 차액은 5
11, 8짜리 소를 사기 위해 이 소를 포기해야 하는가?
차액이 더 큰애가 나타나면 양보를 하는 것이 맞다
아니 다 heappush로 어떻게 때리면 될 것 같은데 감이 안잡히네 피곤해서 그런가 으으그으으그으극
'''