# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        ret = ListNode()
        last = ret
        tens = 0
        ones = 0
        while(l1 and l2):
            add_digits = l1.val + l2.val + tens
            tens = add_digits // 10
            ones = add_digits % 10
            last.next = ListNode(ones)
            last = last.next
            l1 = l1.next
            l2 = l2.next

        l = l1 if l1 else l2
        while(l):
            add_digits = l.val + tens
            tens = add_digits // 10
            ones = add_digits % 10
            last.next = ListNode(ones)
            last = last.next
            l = l.next
        
        if tens:
            last.next = ListNode(tens)
        
        return ret.next