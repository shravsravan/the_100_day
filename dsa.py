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

class Solution: 
    def containsDuplicate(self, nums: List[int]) -> bool: 
        nums.sort() 
        for i in range(1, len(nums)): 
            if nums[i] == nums[i - 1]: 
                return True 
            return False
# Time Complexity: O(n log n) due to sorting
# Space Complexity: O(1) if we ignore the space taken by sorting algorithm

#======================================================================================================================================================
#======================================================================================================================================================

#242. Valid Anagram
#https://leetcode.com/problems/valid-anagram/
from collections import Counter
class Solution: 
    def isAnagram(self, s: str, t: str) -> bool: 
        return Counter(s) == Counter(t) 
    #Conunter creates a dictonary with the count of each character in the 
    #string and we can use that to compare both the characters and as it supports unicode too it works perfectly but 
    #it uses extra space
#Time Complexity: O(n) 
#Space Complexity: O(1) as the space used by the counter is limited to the number of characters in the string

class Solution: 
    def isAnagram(self, s: str, t: str) -> bool: 
        if len(s) != len(t): 
            return False 
        count = [0] * 26 #assuming only lowercase letters
        for i in range(len(s)): 
            count[ord(s[i]) - ord('a')] += 1 
            count[ord(t[i]) - ord('a')] -= 1 
        for c in count: 
            if c != 0: 
                return False 
        return True
    
#Time Complexity: O(n)
#Space Complexity: O(1) as the space used by the count array is limited to 26

#======================================================================================================================================================
#======================================================================================================================================================

#1. Two Sum
#https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {}  # Stores number -> its index
        for i, n in enumerate(nums): 
            diff = target - n
            if diff in prevMap:
                return [prevMap[diff], i]
            prevMap[n] = i

#Time Complexity: O(n)
#Space Complexity: O(n)
#======================================================================================================================================================
#======================================================================================================================================================
