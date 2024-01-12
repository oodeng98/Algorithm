def unionFind(x):
    if x != know[x]:
        know[x] = unionFind(know[x])
    return know[x]
        

T = int(input())
for t in range(T):
    N, M = map(int, input().split())
    know = [i for i in range(N + 1)]
    relation = []
    for i in range(M):
        relation.append(tuple(map(int, input().split())))
        
    for a, b in relation:
        aGroup = unionFind(a)
        bGroup = unionFind(b)
        if aGroup != bGroup:
            if aGroup > bGroup:
                know[aGroup] = bGroup
            else:
                know[bGroup] = aGroup
                
    for i in range(1, N + 1):
        unionFind(i)
        
    print(f"#{t+1} {len(set(know[1:]))}")