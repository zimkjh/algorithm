from itertools import combinations


def solution(orders, course):
    answer = []
    for courseNum in course:
        canL = []
        maxCount = 2
        tempAnswer = []
        for order in orders:
            orderL = sorted(list(order))
            canL += list(map("".join, combinations(orderL, courseNum)))
        canSet = list(set(canL))
        for can in canSet:
            if canL.count(can) >= 2:
                if canL.count(can) > maxCount:
                    maxCount = max(maxCount, canL.count(can))
                    tempAnswer = []
                if canL.count(can) >= maxCount:
                    tempAnswer.append(can)
        answer += tempAnswer
    answer = sorted(answer)
    return answer


orders = ["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"]
course = [2, 3, 4]
print(solution(orders, course))

# 2시 40분
