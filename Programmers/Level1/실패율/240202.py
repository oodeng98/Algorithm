def solution(N, stages):
    dic = {}
    for i in stages:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    result = []
    count = len(stages)
    for i in range(1, N+1):
        if i in dic:
            result.append((i, dic[i] / count))
            count -= dic[i]
        else:
            result.append((i, 0))
    result.sort(key=lambda x: x[1], reverse=True)
    answer = [x[0] for x in result]
    return answer