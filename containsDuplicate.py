class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        # We will use a set to track the numbers we have seen
        seen_numbers = set()

        # Iterate over each number in the array
        for number in nums:
            # If the number is already in the set, we found a duplicate
            if number in seen_numbers:
                return True
            # Otherwise, add the number to the set
            seen_numbers.add(number)

        # If no duplicates are found, return False
        return False
