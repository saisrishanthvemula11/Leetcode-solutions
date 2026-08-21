class Solution:
    def findLucky(self, arr: List[int]) -> int:
        freq = {}
        result = []
        for i in range(len(arr)):
            freq[arr[i]] = freq.get(arr[i],0) + 1

        for i,j in freq.items():
            if i == j:
                result.append(i)    
        if not result:
            return -1
        else:
            return max(result)
                
        