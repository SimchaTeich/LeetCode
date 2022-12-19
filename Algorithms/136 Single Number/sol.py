class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # runtime: O(nlogn) but I need O(n)...
        # memory: O(1), so it's OK.
        nums.sort()

        i = 1
        while i < len(nums):
            if nums[i-1] != nums[i]:
                return nums[i-1]
            i += 2

        return nums[-1]