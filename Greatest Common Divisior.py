class Solution:
    def gcdOfStrings(self, string1: str, string2: str) -> str:
        # Get the lengths of both strings
        length1, length2 = len(string1), len(string2)

        # Define a function to check if a given length is a valid divisor
        def is_valid_divisor(length):
            # Check if the length is a valid divisor for both strings
            if length1 % length != 0 or length2 % length != 0:
                return False
            # Calculate how many times the base string should repeat
            repeat_count1, repeat_count2 = length1 // length, length2 // length
            # Get the base string of the given length
            base_string = string1[:length]
            # Check if repeating the base string forms both original strings
            return string1 == repeat_count1 * base_string and string2 == repeat_count2 * base_string

        # Iterate from the minimum length of the two strings down to 1
        for i in range(min(length1, length2), 0, -1):
            # If the current length is a valid divisor, return the corresponding substring
            if is_valid_divisor(i):
                return string1[:i]
        # If no valid length is found, return an empty string
        return ""
