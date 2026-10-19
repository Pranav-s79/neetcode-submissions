class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        freq_count = {}

        for st in strs:
            count = [0] * 26


            #populates the characters within the string into an array
            for ch in st:
                count[ord(ch) - ord('a')] += 1

            key = tuple(count)

            if key in freq_count:
                freq_count[key].append(st)
            else:
                freq_count[key] = [st]
        

        return list(freq_count.values())

            