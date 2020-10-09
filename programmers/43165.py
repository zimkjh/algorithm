def dfs(numberL, nowSum, target):
    global answer
    if len(numberL) == 0:
        if nowSum == target:
            answer += 1
    else:
        newL = numberL[1:]
        dfs(newL, nowSum + numberL[0], target)
        dfs(newL, nowSum - numberL[0], target)


def solution(numbers, target):
    global answer
    answer = 0
    dfs(numbers, 0, target)
    return answer

