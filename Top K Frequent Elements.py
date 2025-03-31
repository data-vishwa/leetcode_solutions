class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
            countNums = Counter(nums)
            # The most important is to understand that we need to give a key
            # Key here is the count of number of time the elemtn was there and then select it
            return sorted(countNums,key = countNums.get,reverse = True)[:k]
