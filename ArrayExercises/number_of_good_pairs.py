'''
Given an array of integers nums, return the number of good pairs.

A pair (i, j) is called good if nums[i] == nums[j] and i < j.

 

Example 1:

Input: nums = [1,2,3,1,1,3]
Output: 4
Explanation: There are 4 good pairs (0,3), (0,4), (3,4), (2,5) 0-indexed.
Example 2:

Input: nums = [1,1,1,1]
Output: 6
Explanation: Each pair in the array are good.
Example 3:

Input: nums = [1,2,3]
Output: 0
'''

from typing import List


def numIdenticalPairs(nums: List[int]) -> int:
    
        good_pairs: int = 0
        n: int = len(nums)

        for i in range(n):
            for j in range(n):
                if i < j and nums[i] == nums[j]:
                    good_pairs += 1

        return good_pairs

