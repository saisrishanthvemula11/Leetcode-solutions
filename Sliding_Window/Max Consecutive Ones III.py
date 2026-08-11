#problem no 1004
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        start = 0
        count_zero = 0
        max_ones = 0

        for end in range(len(nums)):
            if nums[end] == 0:
                count_zero +=1
            while count_zero > k:
                if nums[start] == 0:
                    count_zero -=1
                start +=1
            max_ones = max(max_ones,end - start + 1)
        return max_ones
