class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            num1 = nums[i]
            num2 = target - num1
            
            if num2 in nums[i+1:]:
                return [i, nums.index(num2, i+1)]