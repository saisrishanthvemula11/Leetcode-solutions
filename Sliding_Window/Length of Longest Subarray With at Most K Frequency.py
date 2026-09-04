#2958 
class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        
        # Hashmap to store the frequency of each number
        freq = {}
        
        # Left pointer of the sliding window
        left = 0
        
        # Stores the maximum valid window length found so far
        mwin = 0
        
        # Move the right pointer through the array
        for right in range(len(nums)):
            
            # Add the current element to the hashmap
            # If it already exists, increase its frequency by 1
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            
            # If the frequency of the current element becomes
            # greater than k, shrink the window from the left
            while freq[nums[right]] > k:
                
                # Remove the leftmost element from the window
                freq[nums[left]] -= 1
                
                # Move the left pointer one position forward
                left += 1
            
            # Calculate the current window length
            # Window = nums[left ... right]
            wlen = right - left + 1
            
            # Update the maximum window length
            mwin = max(mwin, wlen)
        
        # Return the longest valid subarray length
        return mwin
                
            
