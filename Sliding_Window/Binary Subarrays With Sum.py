class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        freq = {0:1}
        count = 0
        prefix = 0
        for i in range(len(nums)):
            prefix += nums[i]
            if prefix - goal in freq:
                count += freq[prefix - goal]
            if prefix in freq:
                freq[prefix] +=1
            else:
                freq[prefix] = 1
        return count