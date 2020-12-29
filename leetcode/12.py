answerSheet = ["a", "aa", "aaa", "ab", "b", "ba", "baa", "baaa", "ac"]  # 1, 2, 3, 4, 5, 6, 7, 8, 9


def getResult(num, digit):
    # 3000 -> 3, 3
    if digit == 0:
        return answerSheet[num].replace("a", "I").replace("b", "V").replace("c", "X")
    elif digit == 1:
        return answerSheet[num].replace("a", "X").replace("b", "L").replace("c", "C")
    elif digit == 2:
        return answerSheet[num].replace("a", "C").replace("b", "D").replace("c", "M")
    else:
        return answerSheet[num].replace("a", "M")


class Solution:
    def intToRoman(self, num: int) -> str:
        result = ""
        digit3 = num // 1000
        if digit3 != 0:
            result += getResult(digit3 - 1, 3)
        num -= digit3 * 1000
        digit2 = num // 100
        if digit2 != 0:
            result += getResult(digit2 - 1, 2)
        num -= digit2 * 100
        digit1 = num // 10
        if digit1 != 0:
            result += getResult(digit1 - 1, 1)
        num -= digit1 * 10
        if num != 0:
            result += getResult(num - 1, 0)
        return result

