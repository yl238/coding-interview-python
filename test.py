from utils.adt import Node
from ch02.remove_dups import remove_duplicates_v2
from ch02.kth_to_last import kth_to_last
from ch02.delete_middle import delete_node
from ch02.partition import partition

if __name__ == '__main__':
    node1 = Node(3)
    node2 = Node(5)
    node3 = Node(8)
    node4 = Node(5)
    node5 = Node(10)
    node6 = Node(2)
    node7 = Node(1)

    node1.next = node2 
    node2.next = node3
    node3.next = node4
    node4.next = node5 
    node5.next = node6
    node6.next = node7


    
    head = partition(node1, 6)    
    head.traverse()

        
