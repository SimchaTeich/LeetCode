class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        k = max(len(w) for w in wordDict)
        print(k)
        n = len(s)
        A = [False]*n
        A[-1] = s[-1] in wordDict

        for i in range(n-1 ,-1 , -1):

            for j in range(k+1):
                print(A)
                if i + j <= n-1 and A[i+j] and s[i:i+j] in wordDict or s[i:] in wordDict:
                    A[i] = True
                    break
        
        return A[0]