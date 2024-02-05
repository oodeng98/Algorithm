import math

def solution(n):
    temp = math.sqrt(n)
    if int(temp) == temp:
        return (temp + 1) ** 2
    return -1
