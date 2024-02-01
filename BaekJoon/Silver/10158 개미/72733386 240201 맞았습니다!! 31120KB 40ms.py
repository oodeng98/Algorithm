import sys


input = sys.stdin.readline

w, h = map(int, input().split())
p, q = map(int, input().split())
T = int(input())
print(abs(w - abs((p + T) % (w * 2) - w)), abs(h - abs((q + T) % (h * 2) - h)))