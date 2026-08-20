class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maximum = nums[0]
        sums = nums[0]

        for i in range(1,len(nums)):
            if sums >= 0:
                sums += nums[i]
            else:
                sums = nums[i]
            if sums > maximum:
                maximum = sums
        return maximum
        