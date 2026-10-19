from collections import Counter

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = Counter()
        dict2 = Counter()

        if len(s) != len(t):
            return False

        for ch in s:
            dict1[ch]+=1
        
        for ch in t:
            dict2[ch] +=1

        return dict1 == dict2