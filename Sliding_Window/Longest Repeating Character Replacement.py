#problem no:424 ****** logic
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding Window + Hash Map + Two Pointers
        # Similar to LeetCode 1004: Max Consecutive Ones III

        # freq stores the frequency of each character
        # inside the current sliding window
        freq = {}

        # Stores the maximum valid window length found so far
        win_size = 0

        # Stores the highest frequency of any single character
        # inside the current window
        max_freq = 0

        # Left pointer of the sliding window
        left = 0

        # Move the right pointer through the string
        for i in range(len(s)):

            # Add the current character to the frequency map
            freq[s[i]] = freq.get(s[i], 0) + 1

            # Update the maximum frequency in the current window
            max_freq = max(max_freq, freq[s[i]])

            # Calculate the current window length
            win_len = i - left + 1

            # Characters that need to be replaced
            # = window length - most frequent character count
            #
            # If this is greater than k, the window is invalid,
            # so move the left pointer forward
            while win_len - max_freq > k:

                # Remove the leftmost character from the window
                freq[s[left]] -= 1

                # Move the left pointer forward
                left += 1

                # Recalculate the window length
                win_len = i - left + 1

            # Update the maximum valid window size
            win_size = max(win_size, win_len)

        # Return the longest valid substring length
        return win_size

        
            
        
