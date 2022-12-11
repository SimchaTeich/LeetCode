class Solution:
    def convert(self, s: str, numRows: int) -> str:
        strings = ['']*numRows

        r = -1
        up = True
        for l in s:

            if up and r + 1 < numRows:
                r += 1
            elif up:
                up = False
                r -= 1
            elif r - 1 >= 0:
                r -= 1
            else:
                r += 1
                up = True

            strings[r] += l

        return ''.join(strings)