def solution(a, b):
    a, b = min(a, b), max(a, b)
    return (a + b) / 2 * (b - a + 1)