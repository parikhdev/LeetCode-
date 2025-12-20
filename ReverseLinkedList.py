class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def create_linked_list(arr):
    if not arr: return None
    head = ListNode(arr[0])
    current = head
    for value in arr[1:]:
        current.next = ListNode(value)
        current = current.next
    return head

def reverseList(head):
    cur = head
    prev = None
    while cur:
        temp = cur.next
        cur.next = prev
        prev = cur
        cur = temp
    return prev


if __name__ == "__main__":
    my_input = [1, 2, 3, 4, 5] 
    linked_list_head = create_linked_list(my_input)
    reversed_head =reverseList(linked_list_head)
    print("Output:")
    while reversed_head:
        print(reversed_head.val, end=" -> ")
        reversed_head = reversed_head.next
    print("None")