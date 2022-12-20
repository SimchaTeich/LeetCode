class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # runtime: O(n)
        # memory without nums list itself: O(1)
        
        num = 0
        for n in nums:
            num ^= n

        return num