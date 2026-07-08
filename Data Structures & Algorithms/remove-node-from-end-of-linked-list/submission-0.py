# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        count = 0
        while temp is not None:
            count += 1
            temp = temp.next
        k = count - n
        temp = head
        if k == 0:
            head = head.next
            return head
        
        i = 0
        prev = None
        while i < k:
            prev = temp
            temp = temp.next
            i+=1
        prev.next = temp.next
        return head