import sys

sys.stdin = open('input.txt')
T = int(input())
for t in range(1, T+1):
    _, n = input().split()
    str_to_int = {"ZRO": 0, "ONE": 1, "TWO": 2, "THR": 3, "FOR": 4, "FIV": 5, "SIX": 6, "SVN": 7, "EGT": 8, "NIN": 9}
    int_to_str = {0: "ZRO", 1: "ONE", 2: "TWO", 3: "THR", 4: "FOR", 5: "FIV", 6: "SIX", 7: "SVN", 8: "EGT", 9: "NIN"}
    temp_array = [0 for _ in range(10)]
    for i in input().split():
        temp_array[str_to_int[i]] += 1
    print(f"#{t}")
    for i in range(10):
        for j in range(temp_array[i]):
            print(int_to_str[i], end=' ')
    print()