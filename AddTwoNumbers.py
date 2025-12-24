class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy_head = ListNode()
        carry = 0
        current_node = dummy_head
        while l1 or l2 or carry:
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            total_sum = digit1 + digit2 + carry
            carry, digit_value = divmod(total_sum, 10)
            current_node.next = ListNode(digit_value)
            current_node = current_node.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        return dummy_head.next
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
    ([2, 4, 3], [5, 6, 4]),
    ([0], [0]),
    ([9, 9, 9], [1])
]
sol = Solution()
for l1_list, l2_list in inputs:
    l1 = toLL(l1_list)
    l2 = toLL(l2_list)
    result = sol.addTwoNumbers(l1, l2)
    print(f"Input: l1 = {l1_list}, l2 = {l2_list}")
    print("Output:", toList(result))
    print()
