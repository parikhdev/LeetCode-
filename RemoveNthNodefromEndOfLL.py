class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head, n):
        dummy = ListNode()
        dummy.next = head
        behind = ahead = dummy
        for _ in range(n + 1):
            ahead = ahead.next
        while ahead:
            behind = behind.next
            ahead = ahead.next
        behind.next = behind.next.next
        return dummy.next
def toLL(lst):
    dummy = ListNode()
    cur = dummy
    for x in lst:
        cur.next = ListNode(x)
        cur = cur.next
    return dummy.next
def toList(head):
    res = []
    while head:
        res.append(head.val)
        head = head.next
    return res
inputs = [
    ([1, 2, 3, 4, 5], 2),
    ([1], 1),
    ([1, 2], 1),
    ([1, 2], 2)
]

sol = Solution()

for head_list, n in inputs:
    head = toLL(head_list)
    result = sol.removeNthFromEnd(head, n)
    print(f"Input: head = {head_list}, n = {n}")
    print("Output:", toList(result))
    print()