def countSame(s, unitNum):
    if len(s) < unitNum:
        return s, 0, len(s)
    unitCount = 1
    unitS = s[:unitNum]
    s = s[unitNum:]
    while s[:unitNum] == unitS:
        unitCount += 1
        s = s[unitNum:]
    return s, unitCount, len(unitS)


def solution(s):
    minLen = len(s)
    for unitNum in range(1, len(s)):
        nowS = s
        resultLength = 0
        while True:
            nowS, unitCount, unitSLen = countSame(nowS, unitNum)
            if unitCount == 0:
                resultLength += unitSLen
                minLen = min(minLen, resultLength)
                break
            if unitCount == 1:
                resultLength += unitSLen
            else:
                resultLength += unitSLen + len(str(unitCount))
        print(unitNum, resultLength)
    return minLen

