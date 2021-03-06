# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


from typing import Optional

# My code
class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False

        fast = head.next
        slow = head
        while fast!= None and fast.next != None:
            if fast == slow:
                return True
            slow = slow.next
            fast = fast.next.next

        return False



# Top vote solution
class Solution1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if head == None or head.next == None:
            return False

        fast = head
        slow = head
        
        while fast.next != None and fast.next.next != None:
            slow = slow.next
            fast = fast.next.next
            if fast == slow:
                return True
            
        return False