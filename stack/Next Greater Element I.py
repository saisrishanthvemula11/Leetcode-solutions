#problem no 3834
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        greater_element = {}
        stack = []

        for i in reversed(nums2):
            while stack and stack[-1] <= i:
                stack.pop()
            if stack:
                greater_element[i] = stack[-1]   
            else:
                greater_element[i] = -1
            stack.append(i)
        answer = []
        for i in nums1:
            answer.append(greater_element[i])
        return answer

        
                



        
