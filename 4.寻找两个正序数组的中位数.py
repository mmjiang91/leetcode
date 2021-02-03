#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        i, j = 0, 0
        count = 0
        n = (len(nums1)+len(nums2))//2
        cur_num = 0
        last_num = 0
        while(count <= n):
            num1 = nums1[i] if i < len(nums1) else 100000000
            num2 = nums2[j] if j < len(nums2) else 100000000
            if num1 == 100000000 == num2:
                break
            last_num = cur_num
            if num1 < num2:
                i += 1
                cur_num = num1
            else:
                j += 1
                cur_num = num2
            count += 1
        
        if ( len(nums1) + len(nums2) ) % 2 == 0:
            return (last_num+cur_num) / 2
        else:
            return cur_num
            
            
# @lc code=end

