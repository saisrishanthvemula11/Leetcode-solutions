#2760
class Solution:
    def longestAlternatingSubarray(self, nums: List[int], threshold: int) -> int:

        # Length of the current valid alternating subarray
        cur = 0

        # Maximum length found so far
        max_len = 0

        # Traverse through the array
        for i in range(len(nums)):

            # If current element exceeds threshold, reset
            if nums[i] > threshold:
                cur = 0

            # Start a new valid subarray
            elif cur == 0:

                # The first element must be even
                if nums[i] % 2 == 0:
                    cur += 1
                else:
                    cur = 0

            # Continue the existing subarray
            else:

                # Current and previous elements must have different parity
                if nums[i] % 2 != nums[i - 1] % 2:
                    cur += 1

                # Alternating pattern is broken
                else:

                    # Current even element can start a new subarray
                    if nums[i] % 2 == 0:
                        cur = 1
                    else:
                        # Odd element cannot start a new subarray
                        cur = 0

            # Update the maximum length
            max_len = max(cur, max_len)

        # Return the longest valid alternating subarray length
        return max_len
