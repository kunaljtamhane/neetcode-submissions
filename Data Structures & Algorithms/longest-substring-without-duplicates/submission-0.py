class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hashset = set()
        left = 0
        maxlen = 0
        for right in range (0, len(s)):
            while s[right] in hashset:
                hashset.remove(s[left])
                left+=1
            hashset.add(s[right])
            maxlen = max(maxlen, right-left+1)
        return maxlen
        
        