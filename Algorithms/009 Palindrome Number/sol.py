class Solution:
    def isPalindrome(self, x: int) -> bool:
       s = str(x)
       h, remain = divmod(len(s), 2)
       return s[:h+remain] == s[h:][::-1]