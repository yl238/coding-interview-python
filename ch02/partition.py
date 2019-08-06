from utils.adt import Node 

def partition(head, x):
    node = head
    tail = node

    while node is not None:
        next = node.next
        if node.val < x:
            node.next = head
            head = node 
        else:
            tail.next = node 
            tail = node 
        node = next 
    tail.next = None 
    return head
