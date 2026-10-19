class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map ={}
        t_map = {}

        if len(s) != len(t):
            return False

        for ch in s:
            if ch in s_map:
                s_map[ch] +=1
            else:
                s_map[ch] = 1

        for ch in t:
            if ch in t_map:
                t_map[ch] +=1
            else:
                t_map[ch] = 1


        return t_map == s_map