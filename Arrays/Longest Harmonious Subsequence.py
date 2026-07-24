class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        wsum = 0
        msum = 0

        vowel = {'a','e','i','o','u'}

        for i in range(k):
            if s[i] in vowel:
                wsum +=1

        msum = wsum

        for i in range(k,len(s)):
            if s[i-k] in vowel:
                wsum -=1
            if s[i] in vowel:
                wsum +=1
            msum = max(msum,wsum)
        return msum

        