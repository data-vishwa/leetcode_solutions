class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        # First, check if the lengths of the two strings are the same
        # If the lengths are not the same, they cannot be anagrams, so return False
        if len(s) != len(t):
            return False

        # Initialize two dictionaries to count the frequency of each character in both strings
        # We use two separate dictionaries for simplicity, as we can directly compare them later
        # (It is possible to use just one dictionary, but that would complicate the logic)
        char_count_s, char_count_t = {}, {}

        # Iterate through each character in the strings
        # Since the strings are the same length, we can loop through one string's length
        for i in range(len(s)):
            # For string 's', increment the count for the current character 's[i]'
            # If the character doesn't exist in the dictionary, 'get' will return 0 and then add 1
            char_count_s[s[i]] = char_count_s.get(s[i], 0) + 1 

            # Similarly, for string 't', increment the count for the current character 't[i]'
            char_count_t[t[i]] = char_count_t.get(t[i], 0) + 1 
        
        # After counting all characters, compare the two dictionaries
        # If they are equal, both strings have the same character counts and are anagrams
        # If they differ, they are not anagrams, so return the result of this comparison
        return char_count_s == char_count_t
