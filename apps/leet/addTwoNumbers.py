# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
    
class SLinkedList:
    def __init__(self):
        self.headval = None
    def insert(self, value):
        New_Node = ListNode(value)
        New_Node.next = self.headval
        self.headval = New_Node

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        p1, p2 = l1, l2
        head = current = ListNode(0)
        
        carry = 0
        while (p1 is not None or p2 is not None or carry > 0):
            p1_val = p1.val if p1 is not None else 0
            p2_val = p2.val if p2 is not None else 0
            value = (p1_val + p2_val + carry) % 10
            carry = (p1_val + p2_val + carry) // 10
            current.next = ListNode(value)
            current = current.next
            
            p1 = p1.next if p1 is not None else None
            p2 = p2.next if p2 is not None else None
            
        return head.next


solution = Solution()

l1 = SLinkedList()
l1.insert(2)
l1.insert(4)
l1.insert(3)
l2 = SLinkedList()
l2.insert(5)
l2.insert(6)
l2.insert(4)
result = solution.addTwoNumbers(l1, l2)