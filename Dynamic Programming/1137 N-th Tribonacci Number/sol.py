class Solution:
    def tribonacci(self, n: int) -> int:
        if n <= 1: return n
        if n == 2: return 1

        first = 0
        second = 1
        third = 1
        fourth = first + second + third
        
        for _ in range(4, n+1):
            first = second
            second = third
            third = fourth
            fourth += (first + second) #first + second + third
        
        return fourth