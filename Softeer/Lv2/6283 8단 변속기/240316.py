import sys


str1 = input().strip().replace(' ', '')
if str1 == '12345678':
    print('ascending')
elif str1 == '87654321':
    print('descending')
else:
    print('mixed')