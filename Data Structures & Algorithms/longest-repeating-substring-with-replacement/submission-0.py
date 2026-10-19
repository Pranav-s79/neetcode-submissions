from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = maxim = 0
        window = Counter()
        max_frequency = 0

        for r in range(len(s)):
            window[s[r]] +=1
            max_frequency = max(window.values())
            replacement = (l-r) - max_frequency
            while (r - l + 1) - max_frequency > k:
                window[s[l]] -= 1
                l += 1
            maxim = max(maxim, r-l+1)
        return maxim

