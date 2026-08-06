#problem no 503
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ge = [-1]*n
        stack = []

        for i in range(2*n-1,-1,-1):
            current = nums[i%n]
            while stack and stack[-1] <= current:
                stack.pop()
            if i < n:
                if not stack:
                    ge[i] = -1
                else:
                    ge[i] = stack[-1]
            stack.append(current)
        return ge


        
