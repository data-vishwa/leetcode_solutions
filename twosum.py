class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # A dictionary to store numbers as keys and their indices as values
        number_to_index = {}

        # Loop through the list with both index and value
        for current_index, current_value in enumerate(nums):
            # Calculate the required value to reach the target_sum
            required_value = target - current_value

            # Check if the required value is already in the dictionary
            if required_value in number_to_index:
                # If found, return the indices of the required_value and the current_value
                return [number_to_index[required_value], current_index]

            # Otherwise, store the current value with its index in the dictionary
            number_to_index[current_value] = current_index
