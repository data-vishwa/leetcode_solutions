class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Dictionary to hold groups of anagrams
        anagram_groups = {}

        for word in strs:
            # Count the frequency of each character in the word
            word_counter = Counter(word)
            # print(word_counter)
            # Convert the Counter object to a tuple of sorted items (to use as a hashable key)
            key = tuple(sorted(word_counter.items()))
            # print(key)
            # Group words by their character frequency count
            if key in anagram_groups:
                anagram_groups[key].append(word)
                # print(f" key is in anagam groups {anagram_groups}")
            else:
                anagram_groups[key] = [word]
                # print(f" key is not anagam groups {anagram_groups}")

        # Return the grouped anagrams as a list of lists
        return list(anagram_groups.values())
