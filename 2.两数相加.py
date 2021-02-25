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
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0
            sumv = l1_val + l2_val + ahead
            ahead = sumv // 10
            p.next = ListNode(sumv%10)
            p = p.next
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        if ahead>0:
            p.next = ListNode(ahead)
        return head.next
# @lc code=end

