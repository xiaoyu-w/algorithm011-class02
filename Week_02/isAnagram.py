class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        有效的字母异位词
        """
        s_dic, t_dic = {}, {}
        for item in s:
            if item not in s_dic:
                s_dic[item] = 1
            else:
                s_dic[item] += 1
        for item in t:
            if item not in t_dic:
                t_dic[item] = 1
            else:
                t_dic[item] += 1
        return s_dic == t_dic