# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast is not None and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
        return False
        # temp = head
        # my_set = set()
        # while temp is not None:
        #     if temp in my_set:
        #         return True
        #     my_set.add(temp)
        #     temp = temp.next
        # return False
