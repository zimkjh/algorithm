def dfs(start, computers, visited):
    visited[start] = 1
    network = computers[start]
    for i in range(len(network)):
        if network[i] == 1 and i != start and visited[i] == 0:
            dfs(i, computers, visited)


def solution(n, computers):
    visited = [0] * n
    idx = 0
    answer = 0
    while sum(visited) < n:
        if visited[idx] == 0:
            dfs(idx, computers, visited)
            answer += 1
        idx += 1
    return answer

