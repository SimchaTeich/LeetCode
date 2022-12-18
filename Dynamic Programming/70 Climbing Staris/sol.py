class Solution:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n
        
        A = [1]*n
        A[-1] = 1
        A[-2] = 2

        for i in range(3, n+1):
            A[-i] = A[-i+1] + A[-i+2]
        
        return A[0]