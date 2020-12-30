class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        answer = 1
        for i in range(len(nums) - 2):
            for j in range(i + 1, len(nums) - 1):
                currentSum = nums[i] + nums[j]
                neededSum = target - currentSum
                tempL = [x - neededSum for x in nums[j + 1:]]
                tempAbs = [abs(x) for x in tempL]
                idx = tempAbs.index(min(tempAbs))
                tempAnswer = tempL[idx] + currentSum + neededSum
                if target == tempAnswer:
                    return tempAnswer
                elif i == 0 and j == 1:
                    answer = tempAnswer
                elif abs(answer - target) > abs(tempAnswer - target):
                    answer = tempAnswer
        return answer

