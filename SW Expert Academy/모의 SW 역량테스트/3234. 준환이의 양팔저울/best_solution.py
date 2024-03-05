def go(left,right,depth,state):
    if depth == n:
        return 1
    if(D[state]>0):
        return D[state]
    cnt =0
    for i in range(n):
        if not visited[i]:
            visited[i]=True
            cnt+=go(left+mam[i],right,depth+1,state+mul[i])
            if left >= right +mam[i]:
                cnt+=go(left,right+mam[i],depth+1,state+mul[i]*2)
            visited[i] = False;
    D[state] = cnt
    return cnt
 
for cs in range(int(input())):
    ans = 0
    n = int(input())
    mam = list(map(int,input().split()))
    visited = [0]*10
    mul = [1, 3, 9, 27, 81, 243, 729, 2187, 6561,19683]
    D = [0] * (mul[n])
    print("#",cs+1," ",go(0,0,0,0),sep="")