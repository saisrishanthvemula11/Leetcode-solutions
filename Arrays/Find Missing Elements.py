class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        n = set(nums)
        ans = []
        for i in range(min(n),max(n)+1):
            if i not in n:
                ans.append(i)
        return ans


        