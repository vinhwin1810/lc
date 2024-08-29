# def addFun(n:int):
#     if n <=0 :
#         return 0
#     if n == 1:
#         return 2
#     return addFun(n-1) + addFun(n-2)

# print(addFun(6))
    

# The functino is expectyed to return an INTEGER_SIGNLY_LINKEDLIST.
# The function accepts INTEGER_SINGLY_LINKED_LIST head as parameter.

class SinglyLinkedListNode:
    int data
    SinglyLinkedListNode next

def deleteEven(listHead: SinglyLinkedListNode) -> SinglyLinkedListNode:
    if not listHead:
        return None
    
    dummy = SinglyLinkedListNode(0)
    dummy.next = listHead
    current = dummy
    
    while current.next:
        if current.next.data % 2 == 0:
            current.next = current.next.next
        else:
            current = current.next
    
    return dummy.next
