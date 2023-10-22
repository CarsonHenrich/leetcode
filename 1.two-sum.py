# Category: algorithms
# Level: Easy
# Percent: 50.480278%


# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
#
#  
# Example 1:
#
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
#
# Example 2:
#
# Input: nums = [3,2,4], target = 6
# Output: [1,2]
#
#
# Example 3:
#
# Input: nums = [3,3], target = 6
# Output: [0,1]
#
#
#  
# Constraints:
#
#
# 	2 <= nums.length <= 10⁴
# 	-10⁹ <= nums[i] <= 10⁹
# 	-10⁹ <= target <= 10⁹
# 	Only one valid answer exists.
#
#
#  
# Follow-up: Can you come up with an algorithm that is less than O(n²) time complexity?


# Start Code Section ----------------------------------------------------------
class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        """Takes a non-sorted array"""
        i, j = 0, len(nums) - 1
        snums = sorted(nums)
        while j > i:
            sum = snums[i] + snums[j]
            if sum == target:
                if snums[i] != snums[j]:
                    return [nums.index(snums[i]), nums.index(snums[j])]
                a = nums.index(snums[i])
                b = nums.index(snums[j], a + 1)
                return [a, b]
            if sum > target:
                j -= 1
            else:
                i += 1
        return []

# End Code Section ------------------------------------------------------------
