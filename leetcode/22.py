answerDict = {}


def getTempAnswer(baseL):
    answerL = []
    for base in baseL:
        answerL.append("(" + base + ")")
        answerL.append("()" + base)
        answerL.append(base + "()")
    return sorted(list(set(answerL)))


def addParen(num1, num2):
    list1 = answerDict[num1]
    list2 = answerDict[num2]
    answerSet = set()
    for l1 in list1:
        for l2 in list2:
            answerSet.add(l1 + l2)
    return sorted(list(answerSet))


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        answerDict[1] = ["()"]
        answerDict[2] = getTempAnswer(answerDict[1])
        answerDict[3] = getTempAnswer(answerDict[2])
        if n <= 3:
            return answerDict[n]
        for i in range(4, n + 1):
            tempL = getTempAnswer(answerDict[i - 1])
            for j in range(2, i - 1):
                tempL += addParen(j, i - j)
            answerDict[i] = sorted(list(set(tempL)))
        return answerDict[n]

