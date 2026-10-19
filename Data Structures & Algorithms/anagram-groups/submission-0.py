class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dictionary = {} #creates new dict
        
        for word in strs:
            key =''.join(sorted(word)) #creates a sorted string for word
            if (key not in dictionary):
                dictionary[key] =[]
            dictionary[key].append(word)

        anagram_list = []
        for keys in dictionary:
            anagram_list.append(dictionary[keys])  


        return anagram_list        




            

