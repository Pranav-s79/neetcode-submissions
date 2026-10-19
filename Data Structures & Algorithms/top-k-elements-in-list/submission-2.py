from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        f = Counter(nums)

        #{num : freq}

        #sorted: iterable, function, reverse
        res = sorted(f.keys(), key = lambda x:f[x], reverse = True)

        return res[:k]