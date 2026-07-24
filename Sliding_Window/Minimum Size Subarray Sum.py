class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        low = 0
        mwindow = float('inf')
        csum = 0

        for high in range(len(nums)):
            csum += nums[high]
            while csum >= target:
                cwin_len = high - low + 1
                mwindow = min(mwindow,cwin_len)
                csum -= nums[low]
                low +=1

        return 0 if mwindow == float('inf') else mwindow
        
        