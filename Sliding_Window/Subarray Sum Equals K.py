class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        prefix = 0 
        freq = {0:1}

        for i in nums:
            prefix += i
            if prefix - k in freq:
                count +=freq[prefix - k]
            if prefix in freq:
                freq[prefix] +=1
            else:
                freq[prefix] = 1
        return count
                