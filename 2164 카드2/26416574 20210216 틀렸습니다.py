import sys
import math
input = sys.stdin.readline

num = int(input())
if num == 1:
    print(1)
else:
    print((num - int(math.log(num, 2)) * 2) * 2)