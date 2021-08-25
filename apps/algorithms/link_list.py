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


ll = SLinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)

current_node = ll.headval
while(current_node is not None):
    print("node:"+ str(current_node.val))
    current_node = current_node.next