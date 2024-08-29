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

def sum_of_left_leaves(root: TreeNode) -> int:
    def is_leaf(node: TreeNode) -> bool:
        return node is not None and node.left is None and node.right is None

    def dfs(node: TreeNode) -> int:
        if node is None:
            return 0
        left_sum = dfs(node.left)
        right_sum = dfs(node.right)
        return left_sum + right_sum + (node.val if is_leaf(node.left) else 0)

    return dfs(root)

def compareStrings(s1, s2):
    stack1 = []
    stack2 = []
    
    for char in s1:
        if char == "#":
            if stack1:  # Only pop if stack is not empty
                stack1.pop()
        else:
            stack1.append(char)
    
    for char in s2:
        if char == "#":
            if stack2:  # Only pop if stack is not empty
                stack2.pop()
        else:
            stack2.append(char)
    
    print(stack1)
    print(stack2)
    return 1 if stack1 == stack2 else 0


def playSegments(coins):
    n = len(coins)
    player1_score = 0
    total_score = sum(coins)  # Total score of all coins
    
    for i in range(n):
        # Player 1's turn
        if coins[i] == 1:
            player1_score += 1
        else:
            player1_score -= 1
        
        # Calculate remaining score for Player 2
        remaining_score = total_score - player1_score
        
        # Check if Player 1's score is greater than remaining score for Player 2
        if player1_score > remaining_score:
            return i + 1  # Return the number of segments Player 1 played
    
    # If we've gone through all segments, Player 1 needs to play all of them
    return n
