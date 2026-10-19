class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False

        #populate both dictionaries
        dict_1 = {}
        dict_2 = {}
        for i in s:
            if i not in dict_1:
                dict_1[i] = 1

            else:
                dict_1[i] += 1

        for i in t:
            if i not in dict_2:
                dict_2[i] = 1

            else:
                dict_2[i] += 1
                

        #compare characters and frequencies
        keys_list = list(dict_1.keys())
        for key in keys_list:
            if key not in dict_2:
                return False
            if dict_1[key] != dict_2[key]:
                return False

        return True



