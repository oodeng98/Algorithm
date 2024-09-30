import sys


input = sys.stdin.readline
N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]
houses.sort()