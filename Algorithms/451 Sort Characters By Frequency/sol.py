class Solution:
    def frequencySort(self, s: str) -> str:
        return ''.join(sorted([l*s.count(l) for l in set(s)], key=len, reverse=True))