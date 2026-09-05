#1493 
class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        
        # start = left boundary of the sliding window
        start = 0
        
        # ans = maximum length of subarray found
        ans = 0
        
        # zero_count = number of zeros in the current window
        zero_count = 0
        
        # Expand the window using end
        for end in range(len(nums)):
            
            # If current element is 0, increase zero count
            if nums[end] == 0:
                zero_count += 1
            
            # If there are more than one zero,
            # shrink the window from the left
            while zero_count > 1:
                
                # If the element being removed is 0,
                # decrease the zero count
                if nums[start] == 0:
                    zero_count -= 1
                
                # Move the left boundary forward
                start += 1
            
            # Calculate the valid subarray length.
            # We subtract 1 because one element must be deleted.
            ans = max(ans, end - start)
        
        # Return the maximum length found
        return ans
