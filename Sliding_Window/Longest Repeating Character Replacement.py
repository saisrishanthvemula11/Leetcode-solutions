class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #sliding winsow + hash maps + two poniters    # similar to the problem no 424. max consecutive ones III
        freq = {}
        win_size = 0
        max_freq = 0
        left = 0
        for i in range(len(s)):
            freq[s[i]] = freq.get(s[i],0) + 1
            max_freq = max(max_freq,freq[s[i]])
            win_len = i - left + 1
            while win_len - max_freq > k:
                freq[s[left]] -=1
                left +=1
                win_len = i - left + 1
            win_size = max(win_size,win_len)
            
        return win_size

        
            
        
