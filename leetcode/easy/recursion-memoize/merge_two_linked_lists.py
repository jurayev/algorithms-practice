# Definition for singly-linked list.
class ListNode:
     def __init__(self, x):
         self.val = x
         self.next = None

#TC = O(m+n) SC = (m+n)
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:

        if not l1:
            return l2
        if not l2:
            return l1

        head = ListNode(0)
        if l1.val < l2.val:
            head.val = l1.val
            head.next = self.mergeTwoLists(l1.next, l2)
        else:
            head.val = l2.val
            head.next = self.mergeTwoLists(l1, l2.next)

        return head

ll1 = [1,2,4]
ll2 = [1,3,4]
# 1
l1 = ListNode(1)
l1.next = ListNode(2)
l1.next.next = ListNode(4)

l2 = ListNode(1)
l2.next = ListNode(3)
l2.next.next = ListNode(4)
l2.next.next.next = ListNode(6)

sol = Solution()
output = sol.mergeTwoLists(l1, l2)
print(output.val)
