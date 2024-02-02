def solution(lottos, win_nums):
    count = len(set(lottos) & set(win_nums))
    result = {0: 6, 1: 6, 2: 5, 3: 4, 4: 3, 5: 2, 6: 1}
    zero_count = 0
    for i in lottos:
        if i == 0:
            zero_count += 1    
    answer = [result[count+zero_count], result[count]]
    return answer