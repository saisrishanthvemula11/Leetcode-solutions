class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = []
        result = nums[0] + nums[1] + nums[2]
        mdiff = float('inf')
        for i in range(len(nums) - 2):
            left = i + 1
            right = len(nums) - 1
            while left < right:
                total = nums[i] + nums[left] + nums[right]
                if total == target:
                    return target
                if total < target:
                    left +=1
                else:
                    right -=1
                diff = abs(total - target)
                if diff < mdiff:
                    result = total
                    mdiff = diff
        return result

        
        