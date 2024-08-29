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

def maximumOccuringCharacter(text: str) -> str:
    char_count = {}
    max_count = 0
    max_char = ''

    for char in text:
        char_count[char] = char_count.get(char, 0) + 1
        if char_count[char] > max_count:
            max_count = char_count[char]
            max_char = char
        elif char_count[char] == max_count and text.index(char) < text.index(max_char):
            max_char = char

    return max_char
