#the problem number is 1748
class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        freq = {}
        result = 0

        for i in nums:
            if i in freq:
                freq[i] +=1
            else:
                freq[i] = 1
        for i,j in freq.items():
            if j == 1:
                result +=i
        return result
        

        
