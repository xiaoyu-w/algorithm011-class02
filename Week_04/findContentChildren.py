class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        """
        分发饼干
        """
        g.sort()
        s.sort()
        count, i, j = 0, 0, 0
        while i < len(g) and j < len(s):
            if g[i] <= s[j]:
                count += 1
                i += 1
                j += 1
            else:
                j += 1            
        return count