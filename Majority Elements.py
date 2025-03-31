class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        from collections import Counter
        # Here you just use counter and get most common.
        numCounter = Counter(nums)
        return numCounter.most_common(1)[0][0]

#   Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times.
# You may assume that the majority element always exists in the array.

# Example 1:
# Input: nums = [3,2,3]
# Output: 3

# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2

 
