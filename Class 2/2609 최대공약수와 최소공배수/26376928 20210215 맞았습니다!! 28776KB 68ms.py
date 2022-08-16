one, two = input().split()
one, two = int(one), int(two)
small = min(one, two)
big = max(one, two)
while big % small != 0:
    temp = small
    small = big % small
    big = temp
print(small)
print(int(one * two / small))