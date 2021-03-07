def add(st, x):
    if x not in st:
        st.append(x)


def removes(st, x):
    if x in st:
        st.remove(x)


def check(st, x):
    if x in st:
        print(1)
    else:
        print(0)


def toggle(st, x):
    if x in st:
        st.remove(x)
    else:
        st.append(x)


import sys

input = sys.stdin.readline

num = int(input())
S = []
for i in range(num):
    temp = input().split()
    if temp[0] == 'add':
        add(S, int(temp[1]))
    elif temp[0] == 'remove':
        removes(S, int(temp[1]))
    elif temp[0] == 'check':
        check(S, int(temp[1]))
    elif temp[0] == 'toggle':
        toggle(S, int(temp[1]))
    elif temp[0] == 'all':
        S = [x for x in range(1, 21)]
    elif temp[0] == 'empty':
        S = []