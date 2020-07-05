class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        字母异位词分组
        """
        res = {}
        for s in strs:
            tag = [0] * 26
            for c in s:
                tag[ord(c) - ord('a')] += 1
            if tuple(tag) not in res:
                res[tuple(tag)] = []
            res[tuple(tag)].append(s)
        return list(res.values())