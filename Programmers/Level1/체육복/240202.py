def solution(n, lost, reserve):
    lost_dic = {i: 0 for i in lost}
    reserve_dic = {i: 0 for i in reserve}
    for r in reserve:
        if r in lost_dic:
            del lost_dic[r]
            del reserve_dic[r]
    new_reserve = sorted(list(reserve_dic.keys()))
    for r in new_reserve:
        if r - 1 in lost_dic:
            del lost_dic[r-1]
        elif r + 1 in lost_dic:
            del lost_dic[r+1]
    answer = n - len(lost_dic)
    return answer