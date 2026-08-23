class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:

        # Dictionary to store how many times each prefix sum has appeared.
        # We start with {0:1} because a prefix sum of 0 exists before the array starts.
        freq = {0:1}

        # Stores the total number of valid subarrays.
        count = 0

        # Keeps track of the running prefix sum.
        prefix = 0

        # Traverse through every element in the array.
        for i in range(len(nums)):

            # Add the current element to the prefix sum.
            prefix += nums[i]

            # Check if there was an earlier prefix sum equal to (prefix - goal).
            # If yes, then the subarray between that position and the current position
            # has a sum equal to 'goal'.
            if prefix - goal in freq:
                count += freq[prefix - goal]

            # Store the current prefix sum in the dictionary.
            # If it already exists, increase its frequency.
            if prefix in freq:
                freq[prefix] += 1
            else:
                freq[prefix] = 1

        # Return the total number of subarrays whose sum is equal to goal.
        return count
