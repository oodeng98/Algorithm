import itertools

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])


T = int(input())

for t in range(T):
    N = int(input())
    lst = list(map(int, input().split()))
    company = (lst[0], lst[1])
    house = (lst[2], lst[3])
    lst = lst[4:]
    customer = []
    for i in range(0, len(lst), 2):
        customer.append((lst[i], lst[i + 1]))

    answer = -1
    for c in itertools.permutations(range(N)):
        temp = 0
        temp += distance(company, customer[c[0]])
        temp += distance(house, customer[c[N - 1]])
        for i in range(N - 1):
            a, b = customer[c[i]], customer[c[i + 1]]
            temp += distance(a, b)
        if answer == -1:
            answer = temp
        else:
            answer = min(answer, temp)
    print(f"#{t+1} {answer}")

"""
1
5
0 0 100 100 70 40 30 10 10 5 90 70 50 20
"""