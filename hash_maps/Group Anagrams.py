class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        count = {}

        for i in strs:
            s = ''.join(sorted(i))
            if s in count:
                count[s].append(i)
            else:
                count[s] = [i]
        return list(count.values())
        