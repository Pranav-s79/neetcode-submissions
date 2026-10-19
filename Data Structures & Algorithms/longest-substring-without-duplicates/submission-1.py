class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = l= r = 0
        curr = 1
        seen = set()

        while r < len(s):
            if not s[r] in seen:
                seen.update(s[r])
                r+= 1
                max_len = max(max_len, curr) 
                curr += 1
                

            else:
                l+=1
                r = l
                curr = 1
                seen = set()

        return max_len

            