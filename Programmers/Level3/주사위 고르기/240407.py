from itertools import product, combinations


def compare(l1, l2):
    dic1, dic2 = {}, {}
    for i in l1:
        if i in dic1:
            dic1[i] += 1
        else:
            dic1[i] = 1
    for i in l2:
        if i in dic2:
            dic2[i] += 1
        else:
            dic2[i] = 1
    lst1 = sorted(list(dic1.keys()))
    lst2 = sorted(list(dic2.keys()))
    len1, len2 = len(lst1), len(lst2)
    index1, index2 = 0, 0
    count1, count2 = 0, 0
    result = 0  # win 기준은 lst1
    while True:
        while index1 < len1 and index2 < len2 and not (lst1[index1] <= lst2[index2]):
            count2 += dic2[lst2[index2]]
            index2 += 1
        if not (index1 < len1 and index2 < len2):
            break
        result += count2 * dic1[lst1[index1]]
        index1 += 1        
    
    while index1 < len1:
        result += count2 * dic1[lst1[index1]]
        index1 += 1
    return result


def solution(dice):
    dice_len = len(dice)
    dices = set(range(dice_len))
    combs = list(combinations(range(dice_len), dice_len // 2))
    max_win = 0
    answer = None
    for comb in combinations(range(dice_len), dice_len // 2):
        p1 = set(comb)
        p2 = dices - p1
        player1 = [dice[i] for i in p1]
        player2 = [dice[i] for i in p2]
        l1 = []
        l2 = []
        for i in product(*player1):
            l1.append(sum(i))
        for i in product(*player2):
            l2.append(sum(i))
        l1.sort(), l2.sort()
        temp = compare(l1, l2)
        if max_win < temp:
            max_win = temp
            answer = sorted([i + 1 for i in p1])
    return answer

'''
1 1 1 1 1 99
2 2 2 2 2 2
총합으로는 불가능
'''