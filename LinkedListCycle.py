class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


def hasCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow is fast:
            return True
    return False

head_list = [1, 2]
pos = -1
nodes = [ListNode(x) for x in head_list]
for i in range(len(nodes) - 1):
    nodes[i].next = nodes[i + 1]
if pos != -1:
    nodes[-1].next = nodes[pos]
print(hasCycle(nodes[0]))
