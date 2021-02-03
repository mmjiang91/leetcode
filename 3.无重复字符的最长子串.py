#
# @lc app=leetcode.cn id=3 lang=python3
#
# [3] 无重复字符的最长子串
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype len: int
        """
        maxLen = 0
        curStr = ""
        for x in s:
            if x not in curStr:
                curStr += x
                if len(curStr) > maxLen:
                    maxLen = len(curStr)
            else:
                curStr = curStr[curStr.rindex(x)+1:] + x
        return maxLen
# @lc code=end

