"""
"""
# N = 4
# trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]

# N = 3
# trust = [[1,3],[2,3],[3,1]]

N = 11
trust = [[1,8],[1,3],[2,8],[2,3],[4,8],[4,3],[5,8],[5,3],[6,8],[6,3],[7,8],[7,3],[9,8],[9,3],[11,8],[11,3]]
def solution(N,trust):
    elim = []
    dic = {}
    for t in trust:
        # print(dic)
        if t[1] not in dic:
            dic[t[1]] = [t[0]]
        else:
            dic[t[1]].append(t[0]) 
        if t[0] in range(1,N+1):
            elim.append(t[0])
    # print(set(range(1,N+1)) - set(elim))
    print(dic)
    if set(range(1,N+1)) - set(elim) != None:
        for i in list(set(range(1,N+1)) - set(elim)):
            # print(dic)
            if i in dic and len(dic[i]) == N-1:
                return i
    return -1

print(solution(N,trust))