#problem no : 2461
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        wsum = 0
        msum = 0
        hash_table = {}

        for i in range(n):
            if nums[i] in hash_table:
                hash_table[nums[i]] +=1
            else:
                hash_table[nums[i]] = 1  
            wsum += nums[i]
            if i >=k:
                wsum -= nums[i-k]
                hash_table[nums[i-k]] -=1

                if hash_table[nums[i-k]] == 0:
                    del hash_table[nums[i-k]]
            if i >=k-1 and len(hash_table) == k:
                msum = max(msum,wsum)
        return msum
 
