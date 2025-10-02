# LeetCode Problem 217: Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
from typing import List

class Solution: 
    def containsDuplicate(self, nums: List[int]) -> bool: 
        hashset = set() #initialize a set to store unique elements
        for n in nums: 
            if n in hashset: 
                return True #return true if the item in the list is already in the set
            hashset.add(n) 
        return False
# Time Complexity: O(n)
# Space Complexity: O(n)

