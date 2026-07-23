class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_set = {}

        for i in range(len(nums)):
            search = target - nums[i]
            if search in hash_set:
                return [i,hash_set[search]]
            hash_set[nums[i]] = i
          