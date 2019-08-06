from utils.adt import Node

def remove_duplicates(head):
    els = []
    node = head
    previous = None
    while node != None:
        if node.val in els:
            previous.next = node.next 
        else:
            els.append(node.val)
        previous = node
        node = node.next


def remove_duplicates_v2(head):
    current = head
    while current != None:
        runner = current
        while runner.next != None:
            if runner.next.val == current.val:
                runner.next = runner.next.next
            else:
                runner = runner.next
        current = current.next 


