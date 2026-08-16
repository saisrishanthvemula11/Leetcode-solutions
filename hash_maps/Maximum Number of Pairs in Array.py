class Solution:
    def numberOfPairs(self, nums: List[int]) -> List[int]:
        freq = {}
        pairs = 0
        leftover = 0
        ans = 0
        for i in range(len(nums)):
            freq[nums[i]] = freq.get(nums[i] , 0) + 1
        for i in freq.values():
            pairs += i//2
            leftover += i%2

        return [pairs,leftover]


            

