#
# @lc app=leetcode.cn id=1 lang=python3
#
# [1] 两数之和
#

# @lc code=start
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        usedDict = {}
        for i, num in enumerate(nums):
            if target - num in usedDict:
                return [usedDict[target-num] , i]
            else:
                usedDict[num] = i
# @lc code=end

