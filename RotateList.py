class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def build_linked_list(arr):
    if not arr: return None
    head = ListNode(arr[0])
    curr = head
    for val in arr[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def print_list(node):
    res = []
    while node:
        res.append(node.val)
        node = node.next
    print(res)

def rotateRight(head, k):
    if not head or not head.next or k == 0:
        return head
    
    last = head
    length = 1
    while last.next:
        last = last.next
        length += 1
        
    k = k % length
    if k == 0:
        return head
    
    last.next = head
    
    steps_to_new_tail = length - k
    new_tail = head
    for _ in range(steps_to_new_tail - 1):
        new_tail = new_tail.next
        
    new_head = new_tail.next
    new_tail.next = None
    
    return new_head

input_data = [1, 2, 3, 4, 5]
linked_head = build_linked_list(input_data)
result = rotateRight(linked_head, 2)
print_list(result)