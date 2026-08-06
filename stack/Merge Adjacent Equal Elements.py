#problem no 3834
class Solution:
    def mergeAdjacent(self, nums: List[int]) -> List[int]:
        stack = []
        for i in nums:
            current = i
            while stack and stack[-1] == current:
                current += stack.pop()
            stack.append(current)
        return stack
        
