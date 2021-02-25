#
# @lc app=leetcode.cn id=4 lang=python3
#
# [4] 寻找两个正序数组的中位数
#

# @lc code=start
class Solution:
    def findkthValue(self, nums1, nums2, k):
        if not nums1:
            return nums2[k-1]
        
        if not nums2:
            return nums1[k-1]

        if k == 1:
            return min(nums1[0], nums2[0])

        m = k//2
        
        if nums1[min(m-1, len(nums1)-1)] >= nums2[min(m-1, len(nums2)-1)]:
            return self.findkthValue(nums1, nums2[m:], k-min(m, len(nums2)))
        else:
            return self.findkthValue(nums1[m:], nums2, k-min(m, len(nums1)))


    def findMedianSortedArrays(self, nums1, nums2):
        m = len(nums1)
        n = len(nums2)
        if (m+n) % 2 == 0:
            return (self.findkthValue(nums1, nums2, (m+n)//2) + self.findkthValue(nums1, nums2, (m+n)//2+1) )/2
        else:
            return self.findkthValue(nums1, nums2, (m+n)//2 + 1)
            
if __name__ == '__main__':
    s = Solution()
    print(s.findMedianSortedArrays([1,2], []))            
# @lc code=end

