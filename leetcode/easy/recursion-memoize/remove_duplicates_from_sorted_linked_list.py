class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    """
    Recursion approach: Time O(n). Space O(1)
    """
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        curr = head
        if curr.next:
            if curr.val == curr.next.val:
                curr = self.deleteDuplicates(curr.next)
            else:
                curr.next = self.deleteDuplicates(curr.next)
        return curr

    def deleteDuplicates_iterative(self, head: ListNode) -> ListNode:
        curr = head
        new_head = curr
        while curr.next:
            if curr.val == curr.next.val:
                prev = curr.next.next
                curr.next = prev
            else:
                curr = curr.next
        return new_head

sol = Solution()

head = ListNode(1)
head.next = ListNode(1)
head.next.next = ListNode(3)
head.next.next.next = ListNode(4)
head.next.next.next.next = ListNode(5)
head.next.next.next.next.next = ListNode(5)


sol.deleteDuplicates_iterative(head)
