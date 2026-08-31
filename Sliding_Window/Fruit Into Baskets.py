# LeetCode 904 - Fruit Into Baskets -------sliding window + prefix sum + hashmaps-----------

class Solution:
    def totalFruit(self, fruits: List[int]) -> int:

        # Dictionary to store the frequency of each fruit
        # Example: {1: 2, 2: 3}
        basket = {}

        # Left pointer of the sliding window
        left = 0

        # Stores the maximum number of fruits we can collect
        max_fruits = 0

        # Move the right pointer through the array
        for right in range(len(fruits)):

            # Add the current fruit to the basket
            # If the fruit already exists, increase its frequency
            # Otherwise, start its frequency from 0 + 1 = 1
            basket[fruits[right]] = basket.get(fruits[right], 0) + 1

            # We can have fruits from at most 2 different types
            # If there are more than 2 types, shrink the window
            while len(basket) > 2:

                # Remove the fruit at the left side of the window
                basket[fruits[left]] -= 1

                # If its frequency becomes 0,
                # completely remove that fruit type from the dictionary
                if basket[fruits[left]] == 0:
                    del basket[fruits[left]]

                # Move the left pointer forward
                left += 1

            # Current window is from left to right
            # Window size = right - left + 1
            # Update the maximum window size
            max_fruits = max(max_fruits, right - left + 1)

        # Return the maximum number of fruits we can collect
        return max_fruits
