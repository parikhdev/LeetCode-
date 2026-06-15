class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteMiddle(head): 
    if not head or not head.next:
        return None
        
    slow = head
    fast = head.next.next
    
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    slow.next = slow.next.next
    return head

ll = lambda arr: ListNode(arr[0], ll(arr[1:])) if arr else None
array = lambda node: [node.val] + array(node.next) if node else []

print(array(deleteMiddle(ll([1,3,4,7,1,2,6]))))