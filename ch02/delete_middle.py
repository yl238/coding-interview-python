from utils.adt import Node 

def delete_node(to_be_deleted):
    node = to_be_deleted
    if node is None or node.next is None:
        return False
    node.val = node.next.val
    node.next = node.next.next 

    return True