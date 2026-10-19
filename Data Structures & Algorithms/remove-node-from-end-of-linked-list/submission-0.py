# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        p1 = head
        len_count = 0
        while p1:
            len_count += 1
            p1 = p1.next
        
        dummy = ListNode(0, head)
        p1 = dummy

        for i in range(len_count - n):
            p1 = p1.next

        
        p1.next = p1.next.next
        


        return dummy.next



