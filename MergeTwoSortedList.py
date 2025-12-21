class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
def toLL(a):
    d = ListNode()
    c = d
    for x in a:
        c.next = ListNode(x)
        c = c.next
    return d.next
def toList(h):
    r = []
    while h:
        r.append(h.val)
        h = h.next
    return r
def mergeTwoLists(list1, list2):
    d = ListNode()
    cur = d
    while list1 and list2:
        if list1.val < list2.val:
            cur.next = list1
            list1 = list1.next
        else:
            cur.next = list2
            list2 = list2.next
        cur = cur.next
    cur.next = list1 or list2
    return d.next

print(toList(mergeTwoLists(toLL([1,2,4]), toLL([1,3,4]))))
