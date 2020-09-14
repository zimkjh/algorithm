import math


def solution(n, s, a, b, fares):
    # 초기 graph 생성
    graph = [[0 for y in range(n + 1)] for x in range(n + 1)]
    for fare in fares:
        graph[fare[0]][fare[1]] = fare[2]
        graph[fare[1]][fare[0]] = fare[2]

    moneyL = [[math.inf, math.inf, math.inf] for x in range(n + 1)]
    visited = []
    queue = [s]
    moneyL[s] = [0, 0, 0]
    while queue:
        now = queue.pop(0)
        if now not in visited:
            visited.append(now)
            for i in range(1, n + 1):
                nowCost = graph[now][i]
                if nowCost > 0:
                    queue.append(i)
                    moneyL[i][0] = min(moneyL[now][0] + nowCost / 2, moneyL[i][0])
                    moneyL[i][1] = min(moneyL[now][1] + nowCost, moneyL[now][1] + nowCost, moneyL[i][1])
                    moneyL[i][2] = min(moneyL[now][0] + nowCost, moneyL[now][1] + nowCost, moneyL[i][2])
    answer = 0
    return answer


n, s, a, b = 6, 4, 6, 2
fares = [[4, 1, 10], [3, 5, 24], [5, 6, 2], [3, 1, 41], [5, 1, 24], [4, 6, 50], [2, 4, 66], [2, 3, 22], [1, 6, 25]]
print(solution(n, s, a, b, fares))

