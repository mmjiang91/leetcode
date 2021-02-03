#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        p = ListNode(None)
        head = p
        ahead = 0
        while l1 or l2:
            if l1 and l2:
                sumv = l1.val+l2.val+ahead
                p.next = ListNode(sumv%10)
                ahead = sumv//10
                l1 = l1.next
                l2 = l2.next
            elif l1:
                p.next = ListNode((ahead+l1.val)%10)
                ahead = (ahead+l1.val)//10
                l1 = l1.next
            elif l2:
                p.next = ListNode((ahead+l2.val)%10)
                ahead = (ahead+l2.val)//10
                l2 = l2.next
            p = p.next
        if ahead>0:
            p.next = ListNode(ahead)
        return head.next
# @lc code=end

