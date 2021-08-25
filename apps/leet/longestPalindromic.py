class Solution:
    def longestPalindrome(self, s: str) -> str:
        hashmap= {}
        start= 0
        max_len= len(s)
        for i in range(max_len):
            if (s[i] in hashmap and start < hashmap[s[i]]):
                str