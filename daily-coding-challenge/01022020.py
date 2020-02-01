"""
This problem was asked by Google.
An XOR linked list is a more memory efficient doubly linked list. Instead of each node holding next and prev fields, it holds a field named both, which is an XOR of the next node and the previous node. Implement an XOR linked list; it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.
If using a language that has no pointers (such as Python), you can assume you have access to get_pointer and dereference_pointer functions that converts between nodes and memory addresses.

"""

#no idea how to do this? 

"""
do this one instead
Given an array nums of integers, return how many of them contain an even number of digits.
https://leetcode.com/problems/find-numbers-with-even-number-of-digits/
"""

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        counter = 0
        for num in nums:
            if len(str(num))%2 == 0:
                counter += 1 
        return counter 
        