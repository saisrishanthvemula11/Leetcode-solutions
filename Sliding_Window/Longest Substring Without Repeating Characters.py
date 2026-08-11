#problem no :3
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # sliding Window + two pointers *****imp
        left = 0
        maxlen = 0

        seen = set()

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left +=1
            seen.add(s[right])
            maxlen = max(maxlen,(right - left) + 1)
        return maxlen
        
