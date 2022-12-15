class Solution:
    def fib(self, n: int) -> int:
        if n <= 1: return n

        first = 0
        second = 1
        third = first + second
        
        for _ in range(3, n+1):
            first = second
            second = third
            third = first + second
        
        return third