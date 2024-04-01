class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        res = ""
        # Each cycle will take 2*(numRows-1) steps.
        increment = 2 * (numRows - 1)

        for r in range(numRows):
            for i in range(r, len(s), increment):
                res += s[i]
                # Check for the middle character in the zigzag pattern except for the first and last row
                if r > 0 and r < numRows - 1 and (i + increment - 2 * r) < len(s):
                    res += s[i + increment - 2 * r]
        return res
