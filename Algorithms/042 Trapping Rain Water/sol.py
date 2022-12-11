class Solution:
    def trap(self, H: List[int]) -> int:
        # vally take at least 3 hights.
        if len(H) < 3:
            return 0
        
        # Finds the highest mountain tops with
        # something like Convex Hull algo.
        stack = [0, 1]   
        for i in range(2, len(H)):
            while len(stack) >= 2 and H[stack[-2]] > H[stack[-1]] and H[stack[-1]] <= H[i]:
                stack.pop(-1)
            stack.append(i)
        
        # fill the vallys was created by indexes of hights inside the stack.
        res = 0
        i = 0
        g = len(stack) - 1
        while i < g:
            m = min(H[stack[i]],H[stack[i+1]])
            
            for k in range(stack[i], stack[i+1]):
                if H[k] < m:
                    res += m - H[k]
            i += 1
        
        return res