class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for string in strs:
            encoded_str+=str(len(string))+"#"+string #follows pattern of length, delimiter, string content

        return encoded_str
    def decode(self, s: str) -> List[str]:
        decoded_list = []
        i = 0
        while i<len(s):
            j = i
            while s[j] != '#':
                j+=1
            
            length = int(s[i:j])

            start = j+1
            end = start + length
            word = s[start:end]
            decoded_list.append(word)

            i = end

        return decoded_list 
