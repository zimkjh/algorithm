def Find(x):
    if par[x] == x:
        return x
    else:
        y = Find(par[x])
        par[x] = y
        return y


def Union(x, y):
    x = Find(x)
    y = Find(y)
    if x != y:
        par[y] = x


def dfs(freeGraph, start):
    # visited, groupGraph
    global groupNum
    global visited
    visited[start] = 1
    groupGraph[start // N][start % N] = groupNum
    graph = freeGraph[start]
    for i in range(len(graph)):
        if visited[i] == 0 and graph[i] == 1:
            dfs(freeGraph, i)


def solution(land, height):
    global N
    N = len(land)
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]
    # 뭉치 만들기
    freeGraph = [[0] * (N * N) for x in range(N * N)]
    for i in range(N):
        for j in range(N):
            if i == j:
                continue
            for d in range(4):
                if i + dx[d] >= N or i + dx[d] < 0:
                    continue
                if j + dy[d] >= N or j + dy[d] < 0:
                    continue
                if abs(land[i][j] - land[i + dx[d]][j + dy[d]]) <= height:
                    freeGraph[i * N + j][(i + dx[d]) * N + (j + dy[d])] = 1
                    freeGraph[(i + dx[d]) * N + (j + dy[d])][i * N + j] = 1
    global visited
    visited = [0] * (N * N)
    global groupGraph
    groupGraph = [[-1] * N for x in range(N)]
    idx = 0
    global groupNum
    groupNum = 0
    while sum(visited) < N * N:
        if visited[idx] == 0:
            dfs(freeGraph, idx)
            groupNum += 1
        idx += 1

    costGraph = []
    # 사다리 비용 구하기
    for i in range(N):
        for j in range(N):
            for d in range(4):
                if i + dx[d] < 0 or i + dx[d] >= N:
                    continue
                if j + dy[d] < 0 or j + dy[d] >= N:
                    continue
                if groupGraph[i][j] == groupGraph[i + dx[d]][j + dy[d]]:
                    continue
                nowGroup = groupGraph[i][j]
                nextGroup = groupGraph[i + dx[d]][j + dy[d]]
                changed = False
                for k in range(len(costGraph)):
                    if costGraph[k][1] == nowGroup and costGraph[k][2] == nextGroup:
                        costGraph[k] = [min(costGraph[k][0], abs(land[i][j] - land[i + dx[d]][j + dy[d]])), nowGroup,
                                        nextGroup]
                        changed = True
                        break
                    if costGraph[k][1] == nextGroup and costGraph[k][2] == nowGroup:
                        costGraph[k] = [min(costGraph[k][0], abs(land[i][j] - land[i + dx[d]][j + dy[d]])), nextGroup,
                                        nowGroup]
                        changed = True
                        break
                if changed == False:
                    costGraph.append([abs(land[i][j] - land[i + dx[d]][j + dy[d]]), nowGroup, nextGroup])

    global par
    par = [x for x in range(groupNum)]
    # 마지막 계산..
    costGraph.sort(key=lambda x: x[0])
    connectNum = 0
    answer = 0

    for i in range(len(costGraph)):
        start = costGraph[i][1]
        end = costGraph[i][2]
        if Find(start) != Find(end):
            Union(start, end)
            answer += costGraph[i][0]
            connectNum += 1
        if connectNum == groupNum - 1:
            break

    return answer

