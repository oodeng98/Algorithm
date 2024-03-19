import sys


input = sys.stdin.readline
M, N, K = map(int, input().split())
secret = ''.join(input().split())
index = 0
if secret in ''.join(input().split()):    
    print('secret')
else:
    print('normal')