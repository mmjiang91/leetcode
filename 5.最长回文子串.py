#
# @lc app=leetcode.cn id=5 lang=python3
#
# [5] 最长回文子串
#

# @lc code=start
class Solution:
    def longestPalindrome(self, s):
        ori_s = s
        s = s.lower()
        count = len(s)
        curLongStr = ''
        for i in range(count):
            j = i - 1
            k = i + 1
            l = 1
            while j>=0 and k<count and s[j] == s[k]:
                j -= 1
                k += 1
                l += 2
            if l>len(curLongStr):
                curLongStr = ori_s[i-(l-1)//2:i+(l-1)//2+1]
            j = i
            k = i + 1
            l = 0
            while j>=0 and k<count and s[j] == s[k]:
                l += 2
                j -= 1
                k += 1
            if l>len(curLongStr):
                curLongStr = ori_s[i-(l//2-1):i+(l//2+1)]
        return curLongStr

if __name__ == '__main__':
    s = Solution()
    #print(s.longestPalindrome('babad'))
# @lc code=end