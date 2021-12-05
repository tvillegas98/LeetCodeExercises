'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.

 

Example 1:

Input: nums = [1,3,5,6], target = 5
Output: 2
Example 2:

Input: nums = [1,3,5,6], target = 2
Output: 1
Example 3:

Input: nums = [1,3,5,6], target = 7
Output: 4
Example 4:

Input: nums = [1,3,5,6], target = 0
Output: 0
Example 5:

Input: nums = [1], target = 0
Output: 0
 

Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums contains distinct values sorted in ascending order.
-104 <= target <= 104
'''

from typing import List

def searchInsert(self, nums: List[int], target: int) -> int:

    def _searchInsert(nums: List[int], s: int, e: int, target: int) -> int:
        if s >= e:
            return s
        m = (s+e) // 2
        if nums[m - 1] < target and target <= nums[m]:
            return m
        elif target > nums[m]:
            return _searchInsert(nums, m+1, e, target)
        return _searchInsert(nums, s, m-1, target)

    return _searchInsert(nums, 0, len(nums), target)