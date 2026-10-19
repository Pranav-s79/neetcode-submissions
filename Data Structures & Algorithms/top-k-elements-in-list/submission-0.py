
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        dictionary = {}
        for num in nums:
            key = num
            if key not in dictionary:
                dictionary[key] = 0
            dictionary[key] += 1

        # #finding max frequency
        # max_val = 0 
        # for amt in dictionary:
        #     if dictionary[amt] > max_val:
        #         max_val = dictionary[amt]

        buckets = [[] for _ in range(len(nums) + 1)]


        #now creating buckets
        for key, freq in dictionary.items():
            buckets[freq].append(key)
        
        res = []
        for freq in range(len(buckets) - 1, 0, -1):
            for num in buckets[freq]:
                res.append(num)
                if len(res) == k:
                    return res


        
      
             


