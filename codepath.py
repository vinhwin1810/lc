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


#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'playSegments' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY coins as parameter.
#

def playSegments(coins):
    max_score = 0
    for i in coins:
        max_score += 1 if i == 1 else -1
    
    play1_score = 0
    
    j = 0
    while play1_score <= max_score / 2 and j < len(coins):
        play1_score += 1 if coins[j] == 1 else -1
        j += 1
    
    return j
        
            

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    coins_count = int(input().strip())

    coins = []

    for _ in range(coins_count):
        coins_item = int(input().strip())
        coins.append(coins_item)

    result = playSegments(coins)

    fptr.write(str(result) + '\n')

    fptr.close()


#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getUmbrellas' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER requirement
#  2. INTEGER_ARRAY sizes
#

def getUmbrellas(requirement, sizes):
    # Write your code here
    dp = [requirement + 1] * (requirement + 1)
    dp[0] = 0

    for a in range(1, requirement + 1):
        for c in sizes:
            if a - c >= 0:
                dp[a] = min(dp[a], 1 + dp[a - c])
    return dp[requirement] if dp[requirement] != requirement + 1 else -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    requirement = int(input().strip())

    sizes_count = int(input().strip())

    sizes = []

    for _ in range(sizes_count):
        sizes_item = int(input().strip())
        sizes.append(sizes_item)

    result = getUmbrellas(requirement, sizes)

    fptr.write(str(result) + '\n')

    fptr.close()


