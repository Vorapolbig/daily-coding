"""
Given head which is a reference node to a singly-linked list. 
The value of each node in the linked list is either 0 or 1. 
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.

 

Example 1:


Input: head = [1,0,1]
Output: 5
Explanation: (101) in base 2 = (5) in base 10
Example 2:

Input: head = [0]
Output: 0
Example 3:

Input: head = [1]
Output: 1
Example 4:

Input: head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
Output: 18880
Example 5:

Input: head = [0,0]
Output: 0
 

Constraints:

The Linked List is not empty.
Number of nodes will not exceed 30.
Each node's value is either 0 or 1.
"""

def solution(head):
    decimal = 0
    for i in range(len(head)-1,-1,-1):
        decimal += head[i] * 2**(len(head)-1-i)
    return decimal

def solution2(head):
    head_list = head
    ans = ''
    while(head_list):
        ans += str(head_list.val)
        head_list = head_list.next
    return(int(ans,2))

head = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
print(solution2(head))
