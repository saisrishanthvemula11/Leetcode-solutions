from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_len = len(s1)
        s2_len = len(s2)

        if s1_len > s2_len:
            return False
        freq_1 = Counter(s1)
        freq_2 = Counter(s2[:s1_len])

        if freq_1 == freq_2:
            return True
        
        for i in range(s1_len,s2_len):
            freq_2[s2[i]] +=1
            freq_2[s2[i - s1_len]] -=1
            if freq_2[s2[i - s1_len]] == 0:
                del freq_2[s2[i - s1_len]]
            if freq_1 == freq_2:
                return True
        return False
    