from utils.adt import Node

def kth_to_last(head, k):
    # k = 0 returns the last element
    if k < 0:
        return None
    p1 = head
    p2 = head
    i = -1 
    while p1 != None:
        p1 = p1.next
        if i < k:
            i+= 1
        else:
            p2 = p2.next
    if i == k:
        return p2.val
    else:
        return None


    