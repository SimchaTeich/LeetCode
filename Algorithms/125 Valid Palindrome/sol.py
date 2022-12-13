class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = ''.join([l.lower() if l.isalnum() else '' for l in s])
        h, remain = divmod(len(s), 2)
        return s[:h+remain] == s[h:][::-1]