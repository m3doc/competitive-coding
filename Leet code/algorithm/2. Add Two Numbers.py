#url: https://leetcode.com/problems/add-two-numbers/
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        # print l1
        # print l2
        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        l3 = ListNode((l1.val + l2.val) % 10)
        head = l3
        carry = (l1.val + l2.val) / 10
        l1 = l1.next
        l2 = l2.next
        while l1 or l2:
            if l1 is not None and l2 is not None:
                # print "here"
                l3.next = ListNode(((l1.val + l2.val) + carry) % 10)
                l3 = l3.next
                # print l3.next.val
                carry = ((l1.val + l2.val) + carry) / 10
                l1 = l1.next
                l2 = l2.next
            elif l1 is None:
                l3.next = ListNode((l2.val + carry) % 10)
                l3 = l3.next
                carry = (l2.val + carry) / 10
                l2 = l2.next
            else:
                l3.next = ListNode((l1.val + carry) % 10)
                l3 = l3.next
                carry = (l1.val + carry) / 10
                l1 = l1.next
        if carry != 0:
            l3.next = ListNode(carry)
        # while head:
        #     print head.val
        #     head = head.next
        # while l3:
        #     print l3.val
        #     l3 = l3.next
        return head

        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
