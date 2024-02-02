def solution(price, money, count):
    for i in range(count):
        money -= price * (i + 1)
    return -min(0, money)