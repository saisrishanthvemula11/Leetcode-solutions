class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_len = 0
        total = 0
        for i in range(len(gain)):
            total += gain[i]
            max_len = max(max_len,total)
        return max_len
        