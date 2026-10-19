from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #count the length of the s1
        #if s2<len(s1) return false
        #sliding window starting from start to finishof s2 -> index + len(s1) <len(s2)
        #create a hashmap of s1 with key: letter -> value:frequency
        #create hashmap for s2 window with same key: letter -> value:frequency
        #check if is the same, if so return true
        #else return false


        if len(s1) > len(s2):
            return False

        s1_count = Counter(s1)
        window = Counter(s2[:len(s1)])

        if s1_count == window:
            return True

        l = 0

        for r in range(len(s1), len(s2)):
            # Add the new character
            window[s2[r]] += 1

            # Remove the left character
            window[s2[l]] -= 1
            if window[s2[l]] == 0:
                del window[s2[l]]

            l += 1

            if window == s1_count:
                return True

        return False
