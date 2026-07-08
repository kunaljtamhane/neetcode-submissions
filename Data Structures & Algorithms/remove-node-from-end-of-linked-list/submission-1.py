class Solution:
	def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
		temp = head
		count = 0
		while temp is not None:
			count = count+1
			temp = temp.next
		k = count - n
		if k == 0:
			head = head.next
			return head
		i = 0
		prev = None
		temp = head
		while i < k:
			prev = temp
			temp = temp.next
			i+=1
		prev.next = temp.next
		return head