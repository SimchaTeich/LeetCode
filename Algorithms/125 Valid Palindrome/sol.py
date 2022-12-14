class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([l.lower() if l.isalnum() else '' for l in s])
        return s == s[::-1]